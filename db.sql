CREATE DATABASE `atividade_flask`;
USE `atividade_flask`;

CREATE TABLE `tb_equipamentos` (
  `id` int PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `nome_equipamento` varchar(255),
  `data_cadastro` datetime,
  `valor_equipamento` double,
  `capacidade_armazenamento` double,
  `id_marcaequipamento` int,
  `id_processador` int,
  `id_placavideo` int,
  `id_setor` int,
  `created_at` datetime,
  `updated_at` datetime
);

CREATE TABLE `tb_setores` (
  `id` int PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `nome_setor` varchar(255),
  `gerente_setor` varchar(255),
  `sigla_setor` varchar(255),
  `qtde_funcionarios` int
);

CREATE TABLE `tb_processadores` (
  `id` int PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `nome_processador` varchar(255),
  `modelo_processador` varchar(255),
  `arquitetura` varchar(255),
  `clock` double,
  `qtd_cores` int,
  `qtd_threads` int,
  `marca_processador` int
);

CREATE TABLE `tb_placavideo` (
  `id` int PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `nome_placa` varchar(255),
  `modelo_placa` varchar(255),
  `cuda_cores` int,
  `memoria_video` double
);

CREATE TABLE `tb_marcaequipamento` (
  `id` int PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `nome_marca` varchar(255)
);

ALTER TABLE `tb_equipamentos` ADD FOREIGN KEY (`id_setor`) REFERENCES `tb_setores` (`id`);

ALTER TABLE `tb_equipamentos` ADD FOREIGN KEY (`id_processador`) REFERENCES `tb_processadores` (`id`);

ALTER TABLE `tb_equipamentos` ADD FOREIGN KEY (`id_placavideo`) REFERENCES `tb_placavideo` (`id`);

ALTER TABLE `tb_equipamentos` ADD FOREIGN KEY (`id_marcaequipamento`) REFERENCES `tb_marcaequipamento` (`id`);