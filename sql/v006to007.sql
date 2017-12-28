ALTER TABLE `location` ADD `rank` INT NULL AFTER `id`;
ALTER TABLE `location` ADD INDEX (`rank`);
ALTER TABLE `location` ADD `gr_color` VARCHAR(6) NULL AFTER `on_graph`;
