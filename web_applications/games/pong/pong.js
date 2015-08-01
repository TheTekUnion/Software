//constants

var WIDTH = 700;
var HEIGHT = 600;


//mathematical value of pi
var pi = Math.PI;


//ASCII arrow key values
var UpArrow = 38;
var DownArrow = 40;


//canvas variables
var canvas;
var ctx;
var keystate;


//game logic variables
var player;
var ball;
var ai;


//player class with x and y positions, a width and height, and an update and draw function

player = {
	x: null,
	y: null,

	width: 20,
	height: 100,

	update: function () {
		if (keystate[UpArrow]) {
			this.y -= 7;
		}
		if (keystate[DownArrow]) {
			this.y += 7;
		}
		this.y = Math.max(Math.min(this.y, HEIGHT - this.height), 0);
	},

	draw: function () {
		ctx.fillRect(this.x, this.y, this.width, this.height);		
	}

}


//ai class with x and y positions, a width and height, and an update and draw function

ai = {
	x: null,
	y: null,

	width: 20,
	height: 100,

	update: function () {
		var desty = ball.y - (this.height - ball.side) * 0.5;
		this.y += (desty - this.y) * 0.1;
		this.y = Math.max(Math.min(this.y, HEIGHT - this.height), 0);
		
	},

	draw: function () {
		ctx.fillRect(this.x, this.y, this.width, this.height);
	}


}


//ball class complete with its own physics

ball = {
	x: null,
	y: null,
	vel: null,

	side: 20,
	speed: 12,

	//serves the ball towards the specified side

	serve: function (side) {
		//set x and y positioning
		var random = Math.random();
		if (this.side === 1) {
			player.x + player.width;
		} else {
			ai.x - this.side;
		}

		this.y = (HEIGHT - this.side) * random;

		//calculate where the ball will go next depending on the angle of the ball on the paddle
		var phi = 0.1 * pi * (1 - 2 * random);
		//set a vector for the ball
		this.vel = {
			x: side * this.speed * Math.cos(phi),
			y: this.speed * Math.sin(phi)
		}
	},

	//ball physics

	update: function () {
		//update position with current velocity
		this.x += this.vel.x;
		this.y += this.vel.y;

		if (0 > this.y || this.y + this.side > HEIGHT) {
			//calculate right offset
			//inside of the canvas the ball is:
			var offset = this.vel.y < 0 ? 0 - this.y : HEIGHT -(this.y + this.side);

			this.y += 2 * offset;
			//replicate the y velocity
			this.vel.y *= -1;
		}
		//function to find intersection between the two
		//axis aligned bounding boxes (AABB)
		var AABBintersect = function(ax, ay, aw, ah, bx, by, bw, bh) {
			return ax < bx + bw && ay < by + bh && bx < ax + aw && by < ay + ah;
		}

		//check x collision 
		//set direction
		var paddle = this.vel.x < 0 ? player : ai;
		if (AABBintersect(paddle.x, paddle.y, paddle.width, paddle.height, this.x, this.y, this.side, this.side)) {
			//set x positioning
			this.x = paddle === player ? player.x + player.width : ai.x - this.side;
			var n = (this.y + this.side - paddle.y) / (paddle.height + this.side);
			var phi = 0.25 * pi * (2 * n - 1);
			//calculate paddle smash
			var smash = Math.abs(phi) > 0.2 * pi ? 1.5 : 1;
			this.vel.x = smash * (paddle === player ? 1 : -1) * this.speed * Math.cos(phi);
			this.vel.y = smash * this.speed * Math.sin(phi);

		}
		//reset the ball when the ball is outside the canvas
		//set x direction
		if (0 > this.x + this.side || this.x > WIDTH) {
			this.serve (paddle === player ? 1 : -1);
		}

	},
	//draw the ball
	draw: function () {
		ctx.fillRect(this.x, this.y, this.side, this.side);
	}


}


//starts the game

var main = function () {

	//create, initiate, and add the game canvas
	canvas = document.createElement("canvas");
	canvas.width = WIDTH;
	canvas.height = HEIGHT;
	ctx = canvas.getContext("2d");
	document.body.appendChild(canvas);

	keystate = {};

	//keep track of keyboard presses

	document.addEventListener("keydown", function (evt) {
		keystate[evt.keyCode] = true;
	});

	document.addEventListener("keyup", function(evt){
		delete keystate[evt.keyCode];

	});

	init();
	//game loop function
	var loop = function () {

		update();
		draw();

		window.requestAnimationFrame(loop, canvas);

	}
	window.requestAnimationFrame(loop, canvas);
	
	//pauses the game

	

}

//initialize game objects

var init = function() {
	player.x = player.width;
	player.y = (HEIGHT - player.height) / 2;

	ai.x = WIDTH - (player.width + ai.width);
	ai.y = (HEIGHT - ai.height) / 2;

	ball.serve(1);
}

//update game objects
var update = function() {
	ball.update();
	player.update();
	ai.update();



}


//clears the canvas and draws the game objects

var draw = function () {
	ctx.fillRect(0, 0, WIDTH, HEIGHT);

	ctx.save();

	ctx.fillStyle = "#FFFFFF";

	ball.draw();
	player.draw();
	ai.draw();
	//draw the net
	var w = 4;
	var x = (WIDTH - w) * 0.5;
	var y = 0;
	var step = HEIGHT / 20; //number of segments


	while (y < HEIGHT) {
		ctx.fillRect(x, y + step * 0.25, w, step * 0.5);
		y += step;
	}

	ctx.restore();
}


//start and run the game
main();