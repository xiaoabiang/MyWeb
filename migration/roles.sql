create table roles
(
  `id` INT not NULL AUTO_INCREMENT PRIMARY KEY,
  `role_name` VARCHAR(100) not NULL,
  `role_comment` VARCHAR(100),
  `create_at` FLOAT
)


INSERT INTO roles (`role_name`,`role_comment`,`create_at`)
VALUES ('ϵͳ����Ա','��������ϵͳ',1466489980),
('Э��Ա','������鲻�����۵�Ȩ��',1466489980),
('�û�','���з������޸����¡��������ۺ͹�ע�����û���Ȩ�ޡ��������û���Ĭ�Ͻ�ɫ',1466489980),
('�����û�','δ��¼���û����ڳ�����ֻ���Ķ�Ȩ��\r\n�û�',1466489980)