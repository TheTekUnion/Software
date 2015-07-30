package com.thetekunion.moremetalsmod.items.tools.shovels;

import com.thetekunion.moremetalsmod.MoreMetalsMod;

import net.minecraft.creativetab.CreativeTabs;
import net.minecraft.item.ItemSpade;

import net.minecraftforge.fml.common.registry.GameRegistry;

public class ItemSilverShovel extends ItemSpade {
    private String name;

    public ItemSilverShovel(ToolMaterial material, String itemName) {
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
