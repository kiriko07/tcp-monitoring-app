-- initdb/01-init.sql
-- 这个文件定义了 TCP 连接监控的数据库表结构。
-- 使用此脚本可以创建和初始化数据库表。

CREATE TABLE public.tcp_connections_demo (
                                             id int4 DEFAULT nextval('tcp_connections_1_id_seq'::regclass) NOT NULL,
                                             remote_ip varchar(45) NOT NULL,
                                             remote_port int4 NOT NULL,
                                             local_ip varchar(45) NOT NULL,
                                             local_port int4 NOT NULL,
                                             created_at timestamp NOT NULL,
                                             disconnected_at timestamp NULL,
                                             last_active_at timestamp NOT NULL,
                                             CONSTRAINT tcp_connections_pkey_1 PRIMARY KEY (id)
);