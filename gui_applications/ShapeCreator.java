package net.ponderisd.graphics;

import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.ColorPicker;
import javafx.scene.control.ComboBox;
import javafx.scene.layout.HBox;
import javafx.scene.paint.Color;
import javafx.scene.shape.Ellipse;
import javafx.scene.shape.Polygon;
import javafx.scene.shape.Rectangle;
import javafx.stage.Stage;


public class ShapeCreator extends Application {

    Stage window;
    Scene scene;
    Button selectButton;
    ComboBox<String> comboBox;
    ColorPicker cp;
    HBox layout = new HBox();

    //Launch Application
    public static void main(String[] args) {
        launch(args);
    }

    @Override
    public void start(Stage primaryStage) throws Exception {
        //Set up stage
        window = primaryStage;
        window.setTitle("Shape Creator");
        //Create select button
        selectButton = new Button("Select");

        /*
            Create the Color Picker using Oracle's API
            Colors include full RGB scale
            Also set a default color of black

         */
        cp = new ColorPicker();
        cp.setValue(Color.BLACK);


        //Create the ComboBox selection for our shapes
        comboBox = new ComboBox<>();
        comboBox.getItems().addAll(
                "Circle",
                "Oval",
                "Square",
                "Rectangle",
                "Triangle",
                "Pentagon",
                "Hexagon"
        );
        comboBox.setPromptText("Shape");
        selectButton.setOnAction(event -> selectShape(comboBox, cp));
        
        
        layout.getChildren().addAll(cp, comboBox, selectButton);

        //Set up the scene
        scene = new Scene(layout, 900, 400);
        window.setScene(scene);
        window.show();

    }

    //Select a shape from a ComboBox and ColorPicker argument
    private void selectShape(ComboBox<String> shapeList, ColorPicker picker) {
        /*
            Create Shapes
            Options Include:

            Circle
            Oval
            Square
            Rectangle
            Triangle
            Pentagon
            Hexagon
         */

        //Circle
        Ellipse circle = new Ellipse(100, 100);
        circle.setFill(picker.getValue());

        //Oval
        Ellipse oval = new Ellipse(100, 50);
        oval.setFill(picker.getValue());

        //Square
        Rectangle square = new Rectangle(200, 200);
        square.setFill(picker.getValue());

        //Rectangle
        Rectangle rectangle = new Rectangle(200, 100);
        rectangle.setFill(picker.getValue());

        //Triangle
        Polygon triangle = new Polygon();
        triangle.getPoints().setAll(
                0d, 200d,
                100d, 0d,
                200d, 200d
        );
        triangle.setFill(picker.getValue());

        //Pentagon
        Polygon pentagon = new Polygon();
        pentagon.getPoints().setAll(
                100d, 0d,
                0d, 75d,
                40d, 200d,
                160d, 200d,
                200d, 75d

        );
        pentagon.setFill(picker.getValue());

        //Hexagon
        Polygon hexagon = new Polygon();
        hexagon.getPoints().setAll(
                50d, 0d,
                0d, 100d,
                50d, 200d,
                150d, 200d,
                200d, 100d,
                150d, 0d

        );
        hexagon.setFill(picker.getValue());

        //Get the shape choice
        String shape = shapeList.getValue();

        //Add the chosen shape from the combobox to the layout
        if (shape == "Circle") {
            layout.getChildren().add(circle);

        } else if (shape == "Oval") {
            layout.getChildren().add(oval);

        } else if (shape == "Square") {
            layout.getChildren().add(square);

        } else if (shape == "Rectangle") {
            layout.getChildren().add(rectangle);

        } else if (shape == "Triangle") {
            layout.getChildren().add(triangle);

        } else if (shape == "Pentagon") {
            layout.getChildren().add(pentagon);

        } else if (shape == "Hexagon") {
            layout.getChildren().add(hexagon);

        }

    }
}