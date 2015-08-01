package com.thetekunion.moremetalsmod.items.tools.pickaxes;

import com.thetekunion.moremetalsmod.MoreMetalsMod;

import net.minecraft.creativetab.CreativeTabs;
import net.minecraft.item.ItemPickaxe;

import net.minecraftforge.fml.common.registry.GameRegistry;

public class ItemCopperPickaxe extends ItemPickaxe {
    private String name;

    public ItemCopperPickaxe(ToolMaterial material, String itemName) {
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
