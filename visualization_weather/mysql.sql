SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for area
-- ----------------------------
DROP TABLE IF EXISTS `visualization_weather_user`;
CREATE TABLE `visualization_weather_user`  (
                              `id` int(11) NOT NULL AUTO_INCREMENT,
                              `uid` varchar(50) COMMENT '编号' ,
                              `name` varchar(50) COMMENT '姓名' ,
                              `role` varchar(60) COMMENT '角色 0-管理员 1-用户',
                              `gender` varchar(50) COMMENT '性别' ,
                              `age` INTEGER COMMENT '年龄' ,
                              `image` varchar(1024) COMMENT '头像' ,
                              `mobile` varchar(1024) COMMENT '电话' ,
                              `email` varchar(50) COMMENT '账号' ,
                              `username` varchar(50) COMMENT '账号' ,
                              `password` varchar(100) COMMENT '密码',
                              `deleted` INTEGER COMMENT '是否删除',
                              `createDate` datetime COMMENT '创建时间',
                              `updateDate` datetime COMMENT '更新时间',
                              `operator` varchar(60) COMMENT '操作',
                              PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

insert into visualization_weather_user
(uid,name,role,username,password,deleted,createDate,updateDate,operator)
values
    ('989f5a38-40ed-4655-82b9-6cff82cb7830','管理员','0','manager','62cb613f61230d45d45dec87df3be745',0,now(),now(),'989f5a38-40ed-4655-82b9-6cff82cb7831');

-- 气象管理
DROP TABLE IF EXISTS `visualization_weather_content`;
CREATE TABLE `visualization_weather_content`  (
                                 `id` int(11) NOT NULL AUTO_INCREMENT,
                                 `uid` varchar(50) COMMENT '编号' ,
                                 `name` varchar(50) COMMENT '名称' ,
                                 `classification` varchar(50) COMMENT '分类' ,
                                 `alarm` varchar(50) COMMENT '名称' ,
                                 `time` varchar(50) COMMENT '名称' ,
                                 `address` varchar(50) COMMENT '年份' ,
                                 `image` varchar(1024) COMMENT '图片',
                                 `description` varchar(4096) COMMENT '说明' ,
                                 `deleted` INTEGER COMMENT '是否删除',
                                 `createDate` datetime COMMENT '创建时间',
                                 `updateDate` datetime COMMENT '更新时间',
                                 `operator` varchar(60) COMMENT '操作',
                                 PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- 气象分类
DROP TABLE IF EXISTS `visualization_weather_classification`;
CREATE TABLE `visualization_weather_classification`  (
                                 `id` int(11) NOT NULL AUTO_INCREMENT,
                                 `uid` varchar(50) COMMENT '编号' ,
                                 `name` varchar(50) COMMENT '名称' ,
                                 `image` varchar(1024) COMMENT '图片',
                                 `content` varchar(1024) COMMENT '内容',
                                 `description` varchar(1024) COMMENT '说明' ,
                                 `deleted` INTEGER COMMENT '是否删除',
                                 `createDate` datetime COMMENT '创建时间',
                                 `updateDate` datetime COMMENT '更新时间',
                                 `operator` varchar(60) COMMENT '操作',
                                 PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- 气象记录
DROP TABLE IF EXISTS `visualization_weather_record`;
CREATE TABLE `visualization_weather_record`  (
                                 `id` int(11) NOT NULL AUTO_INCREMENT,
                                 `uid` varchar(50) COMMENT '编号' ,
                                 `name` varchar(1024) COMMENT '名称' ,
                                 `amount` varchar(1024) COMMENT '数量',
                                 `price` varchar(1024) COMMENT '价格' ,
                                 `deleted` INTEGER COMMENT '是否删除',
                                 `createDate` datetime COMMENT '创建时间',
                                 `updateDate` datetime COMMENT '更新时间',
                                 `operator` varchar(60) COMMENT '操作',
                                 PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- 气象资讯
DROP TABLE IF EXISTS `visualization_weather_notice`;
CREATE TABLE `visualization_weather_notice`  (
                                 `id` int(11) NOT NULL AUTO_INCREMENT,
                                 `uid` varchar(50) COMMENT '编号' ,
                                 `name` varchar(50) COMMENT '名称' ,
                                 `image` varchar(1024) COMMENT '图片',
                                 `content` varchar(1024) COMMENT '图片',
                                 `description` varchar(1024) COMMENT '说明' ,
                                 `deleted` INTEGER COMMENT '是否删除',
                                 `createDate` datetime COMMENT '创建时间',
                                 `updateDate` datetime COMMENT '更新时间',
                                 `operator` varchar(60) COMMENT '操作',
                                 PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;