package com.thetekunion.moremetalsmod.blocks.ores;

import com.thetekunion.moremetalsmod.MoreMetalsMod;

import net.minecraft.block.Block;
import net.minecraft.block.material.Material;
import net.minecraft.creativetab.CreativeTabs;

import net.minecraftforge.fml.common.registry.GameRegistry;

public class BlockSilverOre extends Block {
    private String name;

    public BlockSilverOre(Material material, String itemName) {
        super(material);
        name = itemName;
        GameRegistry.registerBlock(this, name);
        setUnlocalizedName(MoreMetalsMod.MODID + "_" + name);
        setCreativeTab(CreativeTabs.tabBlock);
        setHardness(3F);
        setResistance(15F);
        setStepSound(soundTypeStone);
        setHarvestLevel("pickaxe", 2);


    }

    public String getName() {
        return name;
    }
}
