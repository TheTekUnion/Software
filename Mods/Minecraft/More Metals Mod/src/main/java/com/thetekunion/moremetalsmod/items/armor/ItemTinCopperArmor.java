package com.thetekunion.moremetalsmod.items.armor;

import com.thetekunion.moremetalsmod.MoreMetalsMod;

import net.minecraft.creativetab.CreativeTabs;
import net.minecraft.entity.Entity;
import net.minecraft.item.ItemArmor;
import net.minecraft.item.ItemStack;

import net.minecraftforge.fml.common.registry.GameRegistry;

public class ItemTinCopperArmor extends ItemArmor {
    private String name;

    public ItemTinCopperArmor(ArmorMaterial material, int armorType, String itemName) {
        super(material, 0, armorType);
        name = itemName;
        GameRegistry.registerItem(this, name);
        setUnlocalizedName(MoreMetalsMod.MODID + "_" + name);
        setCreativeTab(CreativeTabs.tabCombat);
    }

    public String getArmorTexture(ItemStack stack, Entity entity, int slot, String type) {
        if(stack.getItem() == MoreMetalsMod.tin_copper_helmet || stack.getItem() == MoreMetalsMod.tin_copper_chestplate ||
                stack.getItem() == MoreMetalsMod.tin_copper_boots) {
            return MoreMetalsMod.MODID + ":models/armor/tin_copper_layer_1.png";
        } else if(stack.getItem() == MoreMetalsMod.tin_copper_leggings) {
            return MoreMetalsMod.MODID + ":models/armor/tin_copper_layer_2.png";
        } else {
            System.out.println("Error in finding item. ");
            return null;
        }
    }

    public String getName() {
        return name;
    }
}
