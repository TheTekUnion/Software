package com.thetekunion.moremetalsmod.blocks.mineral_blocks;

import com.thetekunion.moremetalsmod.MoreMetalsMod;

import net.minecraft.block.Block;
import net.minecraft.block.material.Material;
import net.minecraft.creativetab.CreativeTabs;

import net.minecraftforge.fml.common.registry.GameRegistry;

public class BlockCopperBlock extends Block {
    private String name;

    public BlockCopperBlock(Material material, String itemName) {
        super(material);
        name = itemName;
        GameRegistry.registerBlock(this, name);
        setUnlocalizedName(MoreMetalsMod.MODID + "_" + name);
        setCreativeTab(CreativeTabs.tabBlock);
        setHardness(5F);
        setResistance(30F);
        setStepSound(soundTypeMetal);
        setHarvestLevel("pickaxe", 1);

    }

    public String getName() {
        return name;
    }
}