/**
 * More Metals Mod for Minecraft Forge
 * The Tek Union 2015
 * Developed by Nate Hill (bignate777)
 * Textures and Models by Chaise Glenn (Chaisemagic101)
 */
package com.thetekunion.moremetalsmod;

import com.thetekunion.moremetalsmod.blocks.mineral_blocks.*;
import com.thetekunion.moremetalsmod.blocks.ores.*;
import com.thetekunion.moremetalsmod.handlers.*;
import com.thetekunion.moremetalsmod.items.armor.*;
import com.thetekunion.moremetalsmod.items.ingots.*;
import com.thetekunion.moremetalsmod.items.tools.axes.*;
import com.thetekunion.moremetalsmod.items.tools.hoes.*;
import com.thetekunion.moremetalsmod.items.tools.pickaxes.*;
import com.thetekunion.moremetalsmod.items.tools.shovels.*;
import com.thetekunion.moremetalsmod.items.tools.swords.*;

import net.minecraft.block.Block;
import net.minecraft.block.material.Material;
import net.minecraft.client.Minecraft;
import net.minecraft.client.renderer.entity.RenderItem;
import net.minecraft.client.resources.model.ModelResourceLocation;
import net.minecraft.creativetab.CreativeTabs;
import net.minecraft.init.Items;
import net.minecraft.item.Item;
import net.minecraft.item.ItemArmor;
import net.minecraft.item.ItemStack;

import net.minecraftforge.common.util.EnumHelper;
import net.minecraftforge.fml.common.Mod;
import net.minecraftforge.fml.common.Mod.EventHandler;
import net.minecraftforge.fml.common.event.FMLInitializationEvent;
import net.minecraftforge.fml.common.event.FMLPreInitializationEvent;
import net.minecraftforge.fml.common.registry.GameRegistry;
import net.minecraftforge.fml.relauncher.Side;

@Mod(modid = MoreMetalsMod.MODID, version = MoreMetalsMod.VERSION)
public class MoreMetalsMod {
    public static final String MODID = "bignate777_moremetalsmod";
    public static final String VERSION = "1.0";

    public static Item bronze_axe;
    public static Item bronze_boots;
    public static Item bronze_chestplate;
    public static Item bronze_helmet;
    public static Item bronze_hoe;
    public static Item bronze_ingot;
    public static Item bronze_leggings;
    public static Item bronze_pickaxe;
    public static Item bronze_shovel;
    public static Item bronze_sword;
    public static Item copper_axe;
    public static Item copper_boots;
    public static Item copper_chestplate;
    public static Item copper_helmet;
    public static Item copper_hoe;
    public static Item copper_ingot;
    public static Item copper_leggings;
    public static Item copper_pickaxe;
    public static Item copper_shovel;
    public static Item copper_sword;
    public static Item platinum_axe;
    public static Item platinum_boots;
    public static Item platinum_chestplate;
    public static Item platinum_helmet;
    public static Item platinum_hoe;
    public static Item platinum_ingot;
    public static Item platinum_leggings;
    public static Item platinum_pickaxe;
    public static Item platinum_shovel;
    public static Item platinum_sword;
    public static Item silver_axe;
    public static Item silver_boots;
    public static Item silver_chestplate;
    public static Item silver_helmet;
    public static Item silver_hoe;
    public static Item silver_ingot;
    public static Item silver_leggings;
    public static Item silver_pickaxe;
    public static Item silver_shovel;
    public static Item silver_sword;
    public static Item tin_copper_axe;
    public static Item tin_copper_boots;
    public static Item tin_copper_chestplate;
    public static Item tin_copper_helmet;
    public static Item tin_copper_hoe;
    public static Item tin_copper_ingot;
    public static Item tin_copper_leggings;
    public static Item tin_copper_pickaxe;
    public static Item tin_copper_shovel;
    public static Item tin_copper_sword;
    public static Item tin_axe;
    public static Item tin_boots;
    public static Item tin_chestplate;
    public static Item tin_helmet;
    public static Item tin_hoe;
    public static Item tin_ingot;
    public static Item tin_leggings;
    public static Item tin_pickaxe;
    public static Item tin_shovel;
    public static Item tin_sword;

    public static Item.ToolMaterial bronze;
    public static Item.ToolMaterial copper;
    public static Item.ToolMaterial platinum;
    public static Item.ToolMaterial silver;
    public static Item.ToolMaterial tin_copper;
    public static Item.ToolMaterial tin;

    public static ItemArmor.ArmorMaterial bronze_armor;
    public static ItemArmor.ArmorMaterial copper_armor;
    public static ItemArmor.ArmorMaterial platinum_armor;
    public static ItemArmor.ArmorMaterial silver_armor;
    public static ItemArmor.ArmorMaterial tin_copper_armor;
    public static ItemArmor.ArmorMaterial tin_armor;

    public static Block bronze_block;
    public static Block copper_block;
    public static Block copper_ore;
    public static Block platinum_block;
    public static Block platinum_ore;
    public static Block silver_block;
    public static Block silver_ore;
    public static Block tin_copper_block;
    public static Block tin_block;
    public static Block tin_ore;

    public static CreativeTabs more_metals_mod_creative_tab;


    @EventHandler
    public void preInit(FMLPreInitializationEvent event) {
        //New Ingots
        bronze_ingot = new ItemBronzeIngot("bronze_ingot");
        copper_ingot = new ItemCopperIngot("copper_ingot");
        platinum_ingot = new ItemPlatinumIngot("platinum_ingot");
        silver_ingot = new ItemSilverIngot("silver_ingot");
        tin_copper_ingot = new ItemTinCopperIngot("tin_copper_ingot");
        tin_ingot = new ItemTinIngot("tin_ingot");

        //New Tool Materials
        bronze = EnumHelper.addToolMaterial("bronze", 2, 308, 7.0F, 2.5F, 14);
        copper = EnumHelper.addToolMaterial("copper", 1, 142, 6.0F, 2.0F, 12);
        platinum = EnumHelper.addToolMaterial("platinum", 3, 1024, 8.0F, 5.0F, 14);
        silver = EnumHelper.addToolMaterial("silver", 2, 189, 10.0F, 1.0F, 18);
        tin_copper = EnumHelper.addToolMaterial("tin_copper", 1, 124, 5.0F, 1.5F, 10);
        tin = EnumHelper.addToolMaterial("tin", 1, 106, 4.0F, 1.0F, 8);

        //New Axes
        bronze_axe = new ItemBronzeAxe(bronze, "bronze_axe");
        copper_axe = new ItemCopperAxe(copper, "copper_axe");
        platinum_axe = new ItemPlatinumAxe(platinum, "platinum_axe");
        silver_axe = new ItemSilverAxe(silver, "silver_axe");
        tin_copper_axe = new ItemTinCopperAxe(tin_copper, "tin_copper_axe");
        tin_axe = new ItemTinAxe(tin, "tin_axe");

        //New Hoes
        bronze_hoe = new ItemBronzeHoe(bronze, "bronze_hoe");
        copper_hoe = new ItemCopperHoe(copper, "copper_hoe");
        platinum_hoe = new ItemPlatinumHoe(platinum, "platinum_hoe");
        silver_hoe = new ItemSilverHoe(silver, "silver_hoe");
        tin_copper_hoe = new ItemTinCopperHoe(tin_copper, "tin_copper_hoe");
        tin_hoe = new ItemTinHoe(tin, "tin_hoe");

        //New Pickaxes 
        bronze_pickaxe = new ItemBronzePickaxe(bronze, "bronze_pickaxe");
        copper_pickaxe = new ItemCopperPickaxe(copper, "copper_pickaxe");
        platinum_pickaxe = new ItemPlatinumPickaxe(platinum, "platinum_pickaxe");
        silver_pickaxe = new ItemSilverPickaxe(silver, "silver_pickaxe");
        tin_copper_pickaxe = new ItemTinCopperPickaxe(tin_copper, "tin_copper_pickaxe");
        tin_pickaxe = new ItemTinPickaxe(tin, "tin_pickaxe");

        //New Shovels 
        bronze_shovel = new ItemBronzeShovel(bronze, "bronze_shovel");
        copper_shovel = new ItemCopperShovel(copper, "copper_shovel");
        platinum_shovel = new ItemPlatinumShovel(platinum, "platinum_shovel");
        silver_shovel = new ItemSilverShovel(silver, "silver_shovel");
        tin_copper_shovel = new ItemTinCopperShovel(tin_copper, "tin_copper_shovel");
        tin_shovel = new ItemTinShovel(tin, "tin_shovel");

        //New Swords 
        bronze_sword = new ItemBronzeSword(bronze, "bronze_sword");
        copper_sword = new ItemCopperSword(copper, "copper_sword");
        platinum_sword = new ItemPlatinumSword(platinum, "platinum_sword");
        silver_sword = new ItemSilverSword(silver, "silver_sword");
        tin_copper_sword = new ItemTinCopperSword(tin_copper, "tin_copper_sword");
        tin_sword = new ItemTinSword(tin, "tin_sword");

        //New Armor Materials
        bronze_armor = EnumHelper.addArmorMaterial("bronze_armor", MODID + ":" + "bronze_armor", 17, new int[] {3, 6, 5, 2}, 14);
        copper_armor = EnumHelper.addArmorMaterial("copper_armor", MODID + ":" + "copper_armor", 11, new int[] {2, 5, 5, 1}, 14);
        platinum_armor = EnumHelper.addArmorMaterial("platinum_armor", MODID + ":" + "platinum_armor", 28, new int[] {3, 7, 6, 2}, 10);
        silver_armor = EnumHelper.addArmorMaterial("silver_armor", MODID + ":" + "silver_armor", 13, new int[] {2, 5, 4, 1}, 21);
        tin_copper_armor = EnumHelper.addArmorMaterial("tin_copper_armor", MODID + ":" + "tin_copper_armor", 9, new int[] {2, 5, 4, 1}, 11);
        tin_armor = EnumHelper.addArmorMaterial("tin_armor", MODID + ":" + "tin_armor", 7, new int[] {2, 5, 3, 1}, 10);

        //New Armor
        //Bronze Armor Set
        bronze_helmet = new ItemBronzeArmor(bronze_armor, 0, "bronze_helmet");
        bronze_chestplate = new ItemBronzeArmor(bronze_armor, 1, "bronze_chestplate");
        bronze_leggings = new ItemBronzeArmor(bronze_armor, 2, "bronze_leggings");
        bronze_boots = new ItemBronzeArmor(bronze_armor, 3, "bronze_boots");

        //Copper Armor Set
        copper_helmet = new ItemCopperArmor(copper_armor, 0, "copper_helmet");
        copper_chestplate = new ItemCopperArmor(copper_armor, 1, "copper_chestplate");
        copper_leggings = new ItemCopperArmor(copper_armor, 2, "copper_leggings");
        copper_boots = new ItemCopperArmor(copper_armor, 3, "copper_boots");

        //Platinum Armor Set
        platinum_helmet = new ItemPlatinumArmor(platinum_armor, 0, "platinum_helmet");
        platinum_chestplate = new ItemPlatinumArmor(platinum_armor, 1, "platinum_chestplate");
        platinum_leggings = new ItemPlatinumArmor(platinum_armor, 2, "platinum_leggings");
        platinum_boots = new ItemPlatinumArmor(platinum_armor, 3, "platinum_boots");

        //Silver Armor Set
        silver_helmet = new ItemSilverArmor(silver_armor, 0, "silver_helmet");
        silver_chestplate = new ItemSilverArmor(silver_armor, 1, "silver_chestplate");
        silver_leggings = new ItemSilverArmor(silver_armor, 2, "silver_leggings");
        silver_boots = new ItemSilverArmor(silver_armor, 3, "silver_boots");

        //Tin-Copper Armor Set
        tin_copper_helmet = new ItemTinCopperArmor(tin_copper_armor, 0, "tin_copper_helmet");
        tin_copper_chestplate = new ItemTinCopperArmor(tin_copper_armor, 1, "tin_copper_chestplate");
        tin_copper_leggings = new ItemTinCopperArmor(tin_copper_armor, 2, "tin_copper_leggings");
        tin_copper_boots = new ItemTinCopperArmor(tin_copper_armor, 3, "tin_copper_boots");

        //Tin Armor Set
        tin_helmet = new ItemTinArmor(tin_armor, 0, "tin_helmet");
        tin_chestplate = new ItemTinArmor(tin_armor, 1, "tin_chestplate");
        tin_leggings = new ItemTinArmor(tin_armor, 2, "tin_leggings");
        tin_boots = new ItemTinArmor(tin_armor, 3, "tin_boots");
        
        //New Ores
        copper_ore = new BlockCopperOre(Material.rock, "copper_ore");
        platinum_ore = new BlockPlatinumOre(Material.rock, "platinum_ore");
        silver_ore = new BlockSilverOre(Material.rock, "silver_ore");
        tin_ore = new BlockTinOre(Material.rock, "tin_ore");

        //New Mineral Blocks
        bronze_block = new BlockBronzeBlock(Material.iron, "bronze_block");
        copper_block = new BlockCopperBlock(Material.iron, "copper_block");
        platinum_block = new BlockPlatinumBlock(Material.iron, "platinum_block");
        silver_block = new BlockSilverBlock(Material.iron, "silver_block");
        tin_copper_block = new BlockTinCopperBlock(Material.iron, "tin_copper_block");
        tin_block = new BlockTinBlock(Material.iron, "tin_block");

    }

    @EventHandler
    public void init(FMLInitializationEvent event) {

        if(event.getSide() == Side.CLIENT) {
            //Render Item
            RenderItem renderItem = Minecraft.getMinecraft().getRenderItem();

            //Render Item Model Mesh for each Item
            //Ingots
            renderItem.getItemModelMesher().register(bronze_ingot, 0, new ModelResourceLocation(MODID + ":" + ((ItemBronzeIngot) bronze_ingot).getName(), "inventory"));
            renderItem.getItemModelMesher().register(copper_ingot, 0, new ModelResourceLocation(MODID + ":" + ((ItemCopperIngot) copper_ingot).getName(), "inventory"));
            renderItem.getItemModelMesher().register(platinum_ingot, 0, new ModelResourceLocation(MODID + ":" + ((ItemPlatinumIngot) platinum_ingot).getName(), "inventory"));
            renderItem.getItemModelMesher().register(silver_ingot, 0, new ModelResourceLocation(MODID + ":" + ((ItemSilverIngot) silver_ingot).getName(), "inventory"));
            renderItem.getItemModelMesher().register(tin_copper_ingot, 0, new ModelResourceLocation(MODID + ":" + ((ItemTinCopperIngot) tin_copper_ingot).getName(), "inventory"));
            renderItem.getItemModelMesher().register(tin_ingot, 0, new ModelResourceLocation(MODID + ":" + ((ItemTinIngot) tin_ingot).getName(), "inventory"));
            
            //Axes
            renderItem.getItemModelMesher().register(bronze_axe, 0, new ModelResourceLocation(MODID + ":" + ((ItemBronzeAxe) bronze_axe).getName(), "inventory"));
            renderItem.getItemModelMesher().register(copper_axe, 0, new ModelResourceLocation(MODID + ":" + ((ItemCopperAxe) copper_axe).getName(), "inventory"));
            renderItem.getItemModelMesher().register(platinum_axe, 0, new ModelResourceLocation(MODID + ":" + ((ItemPlatinumAxe) platinum_axe).getName(), "inventory"));
            renderItem.getItemModelMesher().register(silver_axe, 0, new ModelResourceLocation(MODID + ":" + ((ItemSilverAxe) silver_axe).getName(), "inventory"));
            renderItem.getItemModelMesher().register(tin_copper_axe, 0, new ModelResourceLocation(MODID + ":" + ((ItemTinCopperAxe) tin_copper_axe).getName(), "inventory"));
            renderItem.getItemModelMesher().register(tin_axe, 0, new ModelResourceLocation(MODID + ":" + ((ItemTinAxe) tin_axe).getName(), "inventory"));
            
            //Hoes
            renderItem.getItemModelMesher().register(bronze_hoe, 0, new ModelResourceLocation(MODID + ":" + ((ItemBronzeHoe) bronze_hoe).getName(), "inventory"));
            renderItem.getItemModelMesher().register(copper_hoe, 0, new ModelResourceLocation(MODID + ":" + ((ItemCopperHoe) copper_hoe).getName(), "inventory"));
            renderItem.getItemModelMesher().register(platinum_hoe, 0, new ModelResourceLocation(MODID + ":" + ((ItemPlatinumHoe) platinum_hoe).getName(), "inventory"));
            renderItem.getItemModelMesher().register(silver_hoe, 0, new ModelResourceLocation(MODID + ":" + ((ItemSilverHoe) silver_hoe).getName(), "inventory"));
            renderItem.getItemModelMesher().register(tin_copper_hoe, 0, new ModelResourceLocation(MODID + ":" + ((ItemTinCopperHoe) tin_copper_hoe).getName(), "inventory"));
            renderItem.getItemModelMesher().register(tin_hoe, 0, new ModelResourceLocation(MODID + ":" + ((ItemTinHoe) tin_hoe).getName(), "inventory"));
            
            //Pickaxes
            renderItem.getItemModelMesher().register(bronze_pickaxe, 0, new ModelResourceLocation(MODID + ":" + ((ItemBronzePickaxe) bronze_pickaxe).getName(), "inventory"));
            renderItem.getItemModelMesher().register(copper_pickaxe, 0, new ModelResourceLocation(MODID + ":" + ((ItemCopperPickaxe) copper_pickaxe).getName(), "inventory"));
            renderItem.getItemModelMesher().register(platinum_pickaxe, 0, new ModelResourceLocation(MODID + ":" + ((ItemPlatinumPickaxe) platinum_pickaxe).getName(), "inventory"));
            renderItem.getItemModelMesher().register(silver_pickaxe, 0, new ModelResourceLocation(MODID + ":" + ((ItemSilverPickaxe) silver_pickaxe).getName(), "inventory"));
            renderItem.getItemModelMesher().register(tin_copper_pickaxe, 0, new ModelResourceLocation(MODID + ":" + ((ItemTinCopperPickaxe) tin_copper_pickaxe).getName(), "inventory"));
            renderItem.getItemModelMesher().register(tin_pickaxe, 0, new ModelResourceLocation(MODID + ":" + ((ItemTinPickaxe) tin_pickaxe).getName(), "inventory"));

            //Shovels
            renderItem.getItemModelMesher().register(bronze_shovel, 0, new ModelResourceLocation(MODID + ":" + ((ItemBronzeShovel) bronze_shovel).getName(), "inventory"));
            renderItem.getItemModelMesher().register(copper_shovel, 0, new ModelResourceLocation(MODID + ":" + ((ItemCopperShovel) copper_shovel).getName(), "inventory"));
            renderItem.getItemModelMesher().register(platinum_shovel, 0, new ModelResourceLocation(MODID + ":" + ((ItemPlatinumShovel) platinum_shovel).getName(), "inventory"));
            renderItem.getItemModelMesher().register(silver_shovel, 0, new ModelResourceLocation(MODID + ":" + ((ItemSilverShovel) silver_shovel).getName(), "inventory"));
            renderItem.getItemModelMesher().register(tin_copper_shovel, 0, new ModelResourceLocation(MODID + ":" + ((ItemTinCopperShovel) tin_copper_shovel).getName(), "inventory"));
            renderItem.getItemModelMesher().register(tin_shovel, 0, new ModelResourceLocation(MODID + ":" + ((ItemTinShovel) tin_shovel).getName(), "inventory"));
            
            //Swords
            renderItem.getItemModelMesher().register(bronze_sword, 0, new ModelResourceLocation(MODID + ":" + ((ItemBronzeSword) bronze_sword).getName(), "inventory"));
            renderItem.getItemModelMesher().register(copper_sword, 0, new ModelResourceLocation(MODID + ":" + ((ItemCopperSword) copper_sword).getName(), "inventory"));
            renderItem.getItemModelMesher().register(platinum_sword, 0, new ModelResourceLocation(MODID + ":" + ((ItemPlatinumSword) platinum_sword).getName(), "inventory"));
            renderItem.getItemModelMesher().register(silver_sword, 0, new ModelResourceLocation(MODID + ":" + ((ItemSilverSword) silver_sword).getName(), "inventory"));
            renderItem.getItemModelMesher().register(tin_copper_sword, 0, new ModelResourceLocation(MODID + ":" + ((ItemTinCopperSword) tin_copper_sword).getName(), "inventory"));
            renderItem.getItemModelMesher().register(tin_sword, 0, new ModelResourceLocation(MODID + ":" + ((ItemTinSword) tin_sword).getName(), "inventory"));
            
            //Helmets
            renderItem.getItemModelMesher().register(bronze_helmet, 0, new ModelResourceLocation(MODID + ":" + ((ItemBronzeArmor) bronze_helmet).getName(), "inventory"));
            renderItem.getItemModelMesher().register(copper_helmet, 0, new ModelResourceLocation(MODID + ":" + ((ItemCopperArmor) copper_helmet).getName(), "inventory"));
            renderItem.getItemModelMesher().register(platinum_helmet, 0, new ModelResourceLocation(MODID + ":" + ((ItemPlatinumArmor) platinum_helmet).getName(), "inventory"));
            renderItem.getItemModelMesher().register(silver_helmet, 0, new ModelResourceLocation(MODID + ":" + ((ItemSilverArmor) silver_helmet).getName(), "inventory"));
            renderItem.getItemModelMesher().register(tin_copper_helmet, 0, new ModelResourceLocation(MODID + ":" + ((ItemTinCopperArmor) tin_copper_helmet).getName(), "inventory"));
            renderItem.getItemModelMesher().register(tin_helmet, 0, new ModelResourceLocation(MODID + ":" + ((ItemTinArmor) tin_helmet).getName(), "inventory"));

            //Chestplates
            renderItem.getItemModelMesher().register(bronze_chestplate, 0, new ModelResourceLocation(MODID + ":" + ((ItemBronzeArmor) bronze_chestplate).getName(), "inventory"));
            renderItem.getItemModelMesher().register(copper_chestplate, 0, new ModelResourceLocation(MODID + ":" + ((ItemCopperArmor) copper_chestplate).getName(), "inventory"));
            renderItem.getItemModelMesher().register(platinum_chestplate, 0, new ModelResourceLocation(MODID + ":" + ((ItemPlatinumArmor) platinum_chestplate).getName(), "inventory"));
            renderItem.getItemModelMesher().register(silver_chestplate, 0, new ModelResourceLocation(MODID + ":" + ((ItemSilverArmor) silver_chestplate).getName(), "inventory"));
            renderItem.getItemModelMesher().register(tin_copper_chestplate, 0, new ModelResourceLocation(MODID + ":" + ((ItemTinCopperArmor) tin_copper_chestplate).getName(), "inventory"));
            renderItem.getItemModelMesher().register(tin_chestplate, 0, new ModelResourceLocation(MODID + ":" + ((ItemTinArmor) tin_chestplate).getName(), "inventory"));

            //Leggings
            renderItem.getItemModelMesher().register(bronze_leggings, 0, new ModelResourceLocation(MODID + ":" + ((ItemBronzeArmor) bronze_leggings).getName(), "inventory"));
            renderItem.getItemModelMesher().register(copper_leggings, 0, new ModelResourceLocation(MODID + ":" + ((ItemCopperArmor) copper_leggings).getName(), "inventory"));
            renderItem.getItemModelMesher().register(platinum_leggings, 0, new ModelResourceLocation(MODID + ":" + ((ItemPlatinumArmor) platinum_leggings).getName(), "inventory"));
            renderItem.getItemModelMesher().register(silver_leggings, 0, new ModelResourceLocation(MODID + ":" + ((ItemSilverArmor) silver_leggings).getName(), "inventory"));
            renderItem.getItemModelMesher().register(tin_copper_leggings, 0, new ModelResourceLocation(MODID + ":" + ((ItemTinCopperArmor) tin_copper_leggings).getName(), "inventory"));
            renderItem.getItemModelMesher().register(tin_leggings, 0, new ModelResourceLocation(MODID + ":" + ((ItemTinArmor) tin_leggings).getName(), "inventory"));

            //Boots
            renderItem.getItemModelMesher().register(bronze_boots, 0, new ModelResourceLocation(MODID + ":" + ((ItemBronzeArmor) bronze_boots).getName(), "inventory"));
            renderItem.getItemModelMesher().register(copper_boots, 0, new ModelResourceLocation(MODID + ":" + ((ItemCopperArmor) copper_boots).getName(), "inventory"));
            renderItem.getItemModelMesher().register(platinum_boots, 0, new ModelResourceLocation(MODID + ":" + ((ItemPlatinumArmor) platinum_boots).getName(), "inventory"));
            renderItem.getItemModelMesher().register(silver_boots, 0, new ModelResourceLocation(MODID + ":" + ((ItemSilverArmor) silver_boots).getName(), "inventory"));
            renderItem.getItemModelMesher().register(tin_copper_boots, 0, new ModelResourceLocation(MODID + ":" + ((ItemTinCopperArmor) tin_copper_boots).getName(), "inventory"));
            renderItem.getItemModelMesher().register(tin_boots, 0, new ModelResourceLocation(MODID + ":" + ((ItemTinArmor) tin_boots).getName(), "inventory"));

            
            //Render Item Model Mesh for each Block
            //Ores
            renderItem.getItemModelMesher().register(Item.getItemFromBlock(copper_ore), 0, new ModelResourceLocation(MODID + ":" + ((BlockCopperOre) copper_ore).getName(), "inventory"));
            renderItem.getItemModelMesher().register(Item.getItemFromBlock(platinum_ore), 0, new ModelResourceLocation(MODID + ":" + ((BlockPlatinumOre) platinum_ore).getName(), "inventory"));
            renderItem.getItemModelMesher().register(Item.getItemFromBlock(silver_ore), 0, new ModelResourceLocation(MODID + ":" + ((BlockSilverOre) silver_ore).getName(), "inventory"));
            renderItem.getItemModelMesher().register(Item.getItemFromBlock(tin_ore), 0, new ModelResourceLocation(MODID + ":" + ((BlockTinOre) tin_ore).getName(), "inventory"));
            
            //Mineral Blocks
            renderItem.getItemModelMesher().register(Item.getItemFromBlock(bronze_block), 0, new ModelResourceLocation(MODID + ":" + ((BlockBronzeBlock) bronze_block).getName(), "inventory"));
            renderItem.getItemModelMesher().register(Item.getItemFromBlock(copper_block), 0, new ModelResourceLocation(MODID + ":" + ((BlockCopperBlock) copper_block).getName(), "inventory"));
            renderItem.getItemModelMesher().register(Item.getItemFromBlock(platinum_block), 0, new ModelResourceLocation(MODID + ":" + ((BlockPlatinumBlock) platinum_block).getName(), "inventory"));
            renderItem.getItemModelMesher().register(Item.getItemFromBlock(silver_block), 0, new ModelResourceLocation(MODID + ":" + ((BlockSilverBlock) silver_block).getName(), "inventory"));
            renderItem.getItemModelMesher().register(Item.getItemFromBlock(tin_copper_block), 0, new ModelResourceLocation(MODID + ":" + ((BlockTinCopperBlock) tin_copper_block).getName(), "inventory"));
            renderItem.getItemModelMesher().register(Item.getItemFromBlock(tin_block), 0, new ModelResourceLocation(MODID + ":" + ((BlockTinBlock) tin_block).getName(), "inventory"));
        }

        //Event handler
        MoreMetalsModEventHandler handler = new MoreMetalsModEventHandler();
        GameRegistry.registerWorldGenerator(handler, 0);

        //Shaped Crafting Recipes
        //Axes
        GameRegistry.addRecipe(new ItemStack(bronze_axe),
                "XX ",
                "XY ",
                " Y ",
                'X', bronze_ingot,
                'Y', Items.stick
        );
        GameRegistry.addRecipe(new ItemStack(copper_axe),
                "XX ",
                "XY ",
                " Y ",
                'X', copper_ingot,
                'Y', Items.stick
        );
        GameRegistry.addRecipe(new ItemStack(platinum_axe),
                "XX ",
                "XY ",
                " Y ",
                'X', platinum_ingot,
                'Y', Items.stick
        );
        GameRegistry.addRecipe(new ItemStack(silver_axe),
                "XX ",
                "XY ",
                " Y ",
                'X', silver_ingot,
                'Y', Items.stick
        );
        GameRegistry.addRecipe(new ItemStack(tin_copper_axe),
                "XX ",
                "XY ",
                " Y ",
                'X', tin_copper_ingot,
                'Y', Items.stick
        );
        GameRegistry.addRecipe(new ItemStack(tin_axe),
                "XX ",
                "XY ",
                " Y ",
                'X', tin_ingot,
                'Y', Items.stick
        );

        //Hoes
        GameRegistry.addRecipe(new ItemStack(bronze_hoe),
                "XX ",
                " Y ",
                " Y ",
                'X', bronze_ingot,
                'Y', Items.stick
        );
        GameRegistry.addRecipe(new ItemStack(copper_hoe),
                "XX ",
                " Y ",
                " Y ",
                'X', copper_ingot,
                'Y', Items.stick
        );
        GameRegistry.addRecipe(new ItemStack(platinum_hoe),
                "XX ",
                " Y ",
                " Y ",
                'X', platinum_ingot,
                'Y', Items.stick
        );
        GameRegistry.addRecipe(new ItemStack(silver_hoe),
                "XX ",
                " Y ",
                " Y ",
                'X', silver_ingot,
                'Y', Items.stick
        );
        GameRegistry.addRecipe(new ItemStack(tin_copper_hoe),
                "XX ",
                " Y ",
                " Y ",
                'X', tin_copper_ingot,
                'Y', Items.stick
        );
        GameRegistry.addRecipe(new ItemStack(tin_hoe),
                "XX ",
                " Y ",
                " Y ",
                'X', tin_ingot,
                'Y', Items.stick
        );

        //Pickaxes
        GameRegistry.addRecipe(new ItemStack(bronze_pickaxe),
                "XXX",
                " Y ",
                " Y ",
                'X', bronze_ingot,
                'Y', Items.stick
        );
        GameRegistry.addRecipe(new ItemStack(copper_pickaxe),
                "XXX",
                " Y ",
                " Y ",
                'X', copper_ingot,
                'Y', Items.stick
        );
        GameRegistry.addRecipe(new ItemStack(platinum_pickaxe),
                "XXX",
                " Y ",
                " Y ",
                'X', platinum_ingot,
                'Y', Items.stick
        );
        GameRegistry.addRecipe(new ItemStack(silver_pickaxe),
                "XXX",
                " Y ",
                " Y ",
                'X', silver_ingot,
                'Y', Items.stick
        );
        GameRegistry.addRecipe(new ItemStack(tin_copper_pickaxe),
                "XXX",
                " Y ",
                " Y ",
                'X', tin_copper_ingot,
                'Y', Items.stick
        );
        GameRegistry.addRecipe(new ItemStack(tin_pickaxe),
                "XXX",
                " Y ",
                " Y ",
                'X', tin_ingot,
                'Y', Items.stick
        );

        //Shovels
        GameRegistry.addRecipe(new ItemStack(bronze_shovel),
                "X",
                "Y",
                "Y",
                'X', bronze_ingot,
                'Y', Items.stick
        );
        GameRegistry.addRecipe(new ItemStack(copper_shovel),
                "X",
                "Y",
                "Y",
                'X', copper_ingot,
                'Y', Items.stick
        );
        GameRegistry.addRecipe(new ItemStack(platinum_shovel),
                "X",
                "Y",
                "Y",
                'X', platinum_ingot,
                'Y', Items.stick
        );
        GameRegistry.addRecipe(new ItemStack(silver_shovel),
                "X",
                "Y",
                "Y",
                'X', silver_ingot,
                'Y', Items.stick
        );
        GameRegistry.addRecipe(new ItemStack(tin_copper_shovel),
                "X",
                "Y",
                "Y",
                'X', tin_copper_ingot,
                'Y', Items.stick
        );
        GameRegistry.addRecipe(new ItemStack(tin_shovel),
                "X",
                "Y",
                "Y",
                'X', tin_ingot,
                'Y', Items.stick
        );

        //Swords
        GameRegistry.addRecipe(new ItemStack(bronze_sword),
                "X",
                "X",
                "Y",
                'X', bronze_ingot,
                'Y', Items.stick
        );
        GameRegistry.addRecipe(new ItemStack(copper_sword),
                "X",
                "X",
                "Y",
                'X', copper_ingot,
                'Y', Items.stick
        );
        GameRegistry.addRecipe(new ItemStack(platinum_sword),
                "X",
                "X",
                "Y",
                'X', platinum_ingot,
                'Y', Items.stick
        );
        GameRegistry.addRecipe(new ItemStack(silver_sword),
                "X",
                "X",
                "Y",
                'X', silver_ingot,
                'Y', Items.stick
        );
        GameRegistry.addRecipe(new ItemStack(tin_copper_sword),
                "X",
                "X",
                "Y",
                'X', tin_copper_ingot,
                'Y', Items.stick
        );
        GameRegistry.addRecipe(new ItemStack(tin_sword),
                "X",
                "X",
                "Y",
                'X', tin_ingot,
                'Y', Items.stick
        );
        
        //Helmets
        GameRegistry.addRecipe(new ItemStack(bronze_helmet),
                "XXX",
                "X X",
                'X', bronze_ingot
        );      
        GameRegistry.addRecipe(new ItemStack(copper_helmet),
                "XXX",
                "X X",
                'X', copper_ingot
        );
        GameRegistry.addRecipe(new ItemStack(platinum_helmet),
                "XXX",
                "X X",
                'X', platinum_ingot
        );
        GameRegistry.addRecipe(new ItemStack(silver_helmet),
                "XXX",
                "X X",
                'X', silver_ingot
        );
        GameRegistry.addRecipe(new ItemStack(tin_copper_helmet),
                "XXX",
                "X X",
                'X', tin_copper_ingot
        );
        GameRegistry.addRecipe(new ItemStack(tin_helmet),
                "XXX",
                "X X",
                'X', tin_ingot
        );
        
        //Chestplates
        GameRegistry.addRecipe(new ItemStack(bronze_chestplate),
                "X X",
                "XXX",
                "XXX",
                'X', bronze_ingot
        );
        GameRegistry.addRecipe(new ItemStack(copper_chestplate),
                "X X",
                "XXX",
                "XXX",
                'X', copper_ingot
        );
        GameRegistry.addRecipe(new ItemStack(platinum_chestplate),
                "X X",
                "XXX",
                "XXX",
                'X', platinum_ingot
        );
        GameRegistry.addRecipe(new ItemStack(silver_chestplate),
                "X X",
                "XXX",
                "XXX",
                'X', silver_ingot
        );
        GameRegistry.addRecipe(new ItemStack(tin_copper_chestplate),
                "X X",
                "XXX",
                "XXX",
                'X', tin_copper_ingot
        );
        GameRegistry.addRecipe(new ItemStack(tin_chestplate),
                "X X",
                "XXX",
                "XXX",
                'X', tin_ingot
        );
        
        //Leggings
        GameRegistry.addRecipe(new ItemStack(bronze_leggings),
                "XXX",
                "X X",
                "X X",
                'X', bronze_ingot
        );
        GameRegistry.addRecipe(new ItemStack(copper_leggings),
                "XXX",
                "X X",
                "X X",
                'X', copper_ingot
        );
        GameRegistry.addRecipe(new ItemStack(platinum_leggings),
                "XXX",
                "X X",
                "X X",
                'X', platinum_ingot
        );
        GameRegistry.addRecipe(new ItemStack(silver_leggings),
                "XXX",
                "X X",
                "X X",
                'X', silver_ingot
        );
        GameRegistry.addRecipe(new ItemStack(tin_copper_leggings),
                "XXX",
                "X X",
                "X X",
                'X', tin_copper_ingot
        );
        GameRegistry.addRecipe(new ItemStack(tin_leggings),
                "XXX",
                "X X",
                "X X",
                'X', tin_ingot
        );

        //Leggings
        GameRegistry.addRecipe(new ItemStack(bronze_boots),
                "X X",
                "X X",
                'X', bronze_ingot
        );
        GameRegistry.addRecipe(new ItemStack(copper_boots),
                "X X",
                "X X",
                'X', copper_ingot
        );
        GameRegistry.addRecipe(new ItemStack(platinum_boots),
                "X X",
                "X X",
                'X', platinum_ingot
        );
        GameRegistry.addRecipe(new ItemStack(silver_boots),
                "X X",
                "X X",
                'X', silver_ingot
        );
        GameRegistry.addRecipe(new ItemStack(tin_copper_boots),
                "X X",
                "X X",
                'X', tin_copper_ingot
        );
        GameRegistry.addRecipe(new ItemStack(tin_boots),
                "X X",
                "X X",
                'X', tin_ingot
        );

        //Mineral Blocks
        GameRegistry.addRecipe(new ItemStack(bronze_block),
                "XXX",
                "XXX",
                "XXX",
                'X', bronze_ingot
        );
        GameRegistry.addRecipe(new ItemStack(copper_block),
                "XXX",
                "XXX",
                "XXX",
                'X', copper_ingot
        );
        GameRegistry.addRecipe(new ItemStack(platinum_block),
                "XXX",
                "XXX",
                "XXX",
                'X', platinum_ingot
        );
        GameRegistry.addRecipe(new ItemStack(silver_block),
                "XXX",
                "XXX",
                "XXX",
                'X', silver_ingot
        );
        GameRegistry.addRecipe(new ItemStack(tin_copper_block),
                "XXX",
                "XXX",
                "XXX",
                'X', tin_copper_ingot
        );
        GameRegistry.addRecipe(new ItemStack(tin_block),
                "XXX",
                "XXX",
                "XXX",
                'X', tin_ingot
        );


        //Shapeless Recipes
        //Tin-Copper Ingot Recipe
        GameRegistry.addShapelessRecipe(new ItemStack(tin_copper_ingot), copper_ingot, tin_ingot);

        //Return Ingots From Mineral Blocks
        GameRegistry.addShapelessRecipe(new ItemStack(bronze_ingot, 9), new ItemStack(bronze_block));
        GameRegistry.addShapelessRecipe(new ItemStack(copper_ingot, 9), new ItemStack(bronze_block));
        GameRegistry.addShapelessRecipe(new ItemStack(platinum_ingot, 9), new ItemStack(platinum_block));
        GameRegistry.addShapelessRecipe(new ItemStack(silver_ingot, 9), new ItemStack(silver_block));
        GameRegistry.addShapelessRecipe(new ItemStack(tin_copper_ingot, 9), new ItemStack(tin_copper_block));
        GameRegistry.addShapelessRecipe(new ItemStack(tin_ingot, 9), new ItemStack(tin_block));


        //Smelting Recipes
        GameRegistry.addSmelting(tin_copper_ingot, new ItemStack(bronze_ingot), .7F);
        GameRegistry.addSmelting(copper_ore, new ItemStack(copper_ingot), .2F);
        GameRegistry.addSmelting(platinum_ore, new ItemStack(platinum_ingot), 1F);
        GameRegistry.addSmelting(silver_ore, new ItemStack(silver_ingot), 1F);
        GameRegistry.addSmelting(tin_ore, new ItemStack(tin_ingot), .2F);
    }
}