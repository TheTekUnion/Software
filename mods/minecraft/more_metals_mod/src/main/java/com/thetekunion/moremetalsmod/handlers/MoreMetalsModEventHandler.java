package com.thetekunion.moremetalsmod.handlers;

import java.util.Random;

import com.thetekunion.moremetalsmod.MoreMetalsMod;

import net.minecraft.block.Block;
import net.minecraft.util.BlockPos;
import net.minecraft.world.World;
import net.minecraft.world.chunk.IChunkProvider;
import net.minecraft.world.gen.feature.WorldGenMinable;

import net.minecraftforge.fml.common.IWorldGenerator;

public class MoreMetalsModEventHandler implements IWorldGenerator {

    @Override
    public void generate(Random random, int chunkX, int chunkZ, World world, IChunkProvider chunkGenerator, IChunkProvider chunkProvider) {
        switch(world.provider.getDimensionId()) {
            case 1: generateEnd(world, random, new BlockPos(chunkX * 16, 64, chunkZ * 16));
                break;
            case 0: generateOverworld(world, random, new BlockPos(chunkX * 16, 64, chunkZ * 16));
                break;
            case -1: generateNether(world, random, new BlockPos(chunkX * 16, 64, chunkZ * 16));
                break;
        }
    }


    private void generateOreInStone(Block block, World world, Random random, BlockPos pos, int maxX, int maxZ, int maxVeinSize, int chancesToSpawn, int minY, int maxY) {
        WorldGenMinable mine = new WorldGenMinable(block.getDefaultState(), maxVeinSize);
        int diffY = maxY - minY;
        for(int x = 0; x < chancesToSpawn; x++) {
            int posX = pos.getX() + random.nextInt(maxX);
            int posY = minY + random.nextInt(diffY);
            int posZ = pos.getZ() + random.nextInt(maxZ);
            BlockPos genPos = new BlockPos(posX, posY, posZ);
            mine.generate(world, random, genPos);
        }
    }


    private void generateEnd(World world, Random random, BlockPos pos) {

    }

    private void generateOverworld(World world, Random random, BlockPos pos) {
        generateOreInStone(MoreMetalsMod.copper_ore, world, random, pos, 16, 16, 4 + random.nextInt(7), 84, 0, 64);
        MoreMetalsMod.copper_ore.dropXpOnBlockBreak(world, pos, random.nextInt(3));
        generateOreInStone(MoreMetalsMod.platinum_ore, world, random, pos, 16, 16, 3 + random.nextInt(6), 6, 0, 18);
        MoreMetalsMod.platinum_ore.dropXpOnBlockBreak(world, pos, random.nextInt((7 - 3) + 1) + 3);
        generateOreInStone(MoreMetalsMod.silver_ore, world, random, pos, 16, 16, 4 + random.nextInt(5), 8, 0, 29);
        //No XP for Silver
        generateOreInStone(MoreMetalsMod.tin_ore, world, random, pos, 16, 16, 4 + random.nextInt(7), 84, 0, 64);
        MoreMetalsMod.tin_ore.dropXpOnBlockBreak(world, pos, random.nextInt(3));

    }

    private void generateNether(World world, Random random, BlockPos pos) {

    }

}
