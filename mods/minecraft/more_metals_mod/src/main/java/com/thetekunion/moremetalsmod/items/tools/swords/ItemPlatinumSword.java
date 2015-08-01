package com.thetekunion.moremetalsmod.items.tools.swords;

import com.thetekunion.moremetalsmod.MoreMetalsMod;

import net.minecraft.creativetab.CreativeTabs;

import net.minecraft.item.ItemSword;

import net.minecraftforge.fml.common.registry.GameRegistry;

public class ItemPlatinumSword extends ItemSword {
    private String name;

    public ItemPlatinumSword(ToolMaterial material, String itemName) {
        super(material);
        name = itemName;
        GameRegistry.registerItem(this, name);
        setUnlocalizedName(MoreMetalsMod.MODID + "_" + name);
        setCreativeTab(CreativeTabs.tabCombat);
    }

    public String getName() {
        return name;
    }
}
