package com.thetekunion.moremetalsmod.items.tools.axes;

import com.thetekunion.moremetalsmod.MoreMetalsMod;

import net.minecraft.creativetab.CreativeTabs;
import net.minecraft.item.ItemAxe;

import net.minecraftforge.fml.common.registry.GameRegistry;

public class ItemPlatinumAxe extends ItemAxe {
    private String name;

    public ItemPlatinumAxe(ToolMaterial material, String itemName) {
        super(material);
        name = itemName;
        GameRegistry.registerItem(this, name);
        setUnlocalizedName(MoreMetalsMod.MODID + "_" + name);
        setCreativeTab(CreativeTabs.tabTools);
    }

    public String getName() {
        return name;
    }
}
