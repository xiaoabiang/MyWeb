create table roles
(
  `id` INT not NULL AUTO_INCREMENT PRIMARY KEY,
  `role_name` VARCHAR(100) not NULL,
  `role_comment` VARCHAR(100),
  `create_at` FLOAT
)


INSERT INTO roles (`role_name`,`role_comment`,`create_at`)
VALUES ('系统管理员','管理整个系统',1466489980),
('协管员','增加审查不当评论的权限',1466489980),
('用户','具有发布和修改文章、发表评论和关注其他用户的权限。这是新用户的默认角色',1466489980),
('匿名用户','未登录的用户。在程序中只有阅读权限\r\n用户',1466489980)