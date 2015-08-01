package com.thetekunion.moremetalsmod.items.ingots;

import com.thetekunion.moremetalsmod.MoreMetalsMod;

import net.minecraft.creativetab.CreativeTabs;
import net.minecraft.item.Item;

import net.minecraftforge.fml.common.registry.GameRegistry;

public class ItemPlatinumIngot extends Item {
    private String name;

    public ItemPlatinumIngot(String itemName) {
        name = itemName;
        GameRegistry.registerItem(this, name);
        setUnlocalizedName(MoreMetalsMod.MODID + "_" + name);
        setCreativeTab(CreativeTabs.tabMaterials);
    }

    public String getName() {
        return name;
    }
}
