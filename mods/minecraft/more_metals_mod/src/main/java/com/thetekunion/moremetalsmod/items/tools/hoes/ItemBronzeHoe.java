package com.thetekunion.moremetalsmod.items.tools.hoes;

import com.thetekunion.moremetalsmod.MoreMetalsMod;

import net.minecraft.creativetab.CreativeTabs;
import net.minecraft.item.ItemHoe;

import net.minecraftforge.fml.common.registry.GameRegistry;

public class ItemBronzeHoe extends ItemHoe {
    private String name;

    public ItemBronzeHoe(ToolMaterial material, String itemName) {
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
