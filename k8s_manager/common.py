# -*- coding: utf-8 -*-

STATUS_VALUE = (
    (1,'上架'),
    (2,'下架'),
    (3,'在线'),
    (4,'离线'),
)

TYPE_VALUE = (
    (1,'内部服务器'),
    (2,'内部虚拟机'),
    (3,'阿里云'),
    (4,'腾讯云'),
    (5,'交换机'),
    (6,'防火墙'),
)

type_list = map(lambda x: x[1], TYPE_VALUE)
status_list = map(lambda x: x[1], STATUS_VALUE)


VERSION_STATUS_VALUE = (    
    (1,'需求收集'),
    (2,'需求评审'),
    (3,'立项'),
    (4,'排期'),
    (5,'开发'),
    (6,'测试'),
    (7,'安全测试'),
    (8,'发布'),
    (9,'验收'),
)

version_status_list = map(lambda x: x[1], VERSION_STATUS_VALUE)


# 通用状态
COMMON_STATUS = (
    ("yes","yes"),
    ("no","no")
)

# 集群部署版本
K8S_VERSION = (
    ("v1.8","v1.8"),
    ("v1.9","v1.9"),
    ("v1.10","v1.10"),
    ("v1.11","v1.11"),
    ("v1.12","v1.12"),
)

# 集群部署模式
K8S_DEPLOY_MODE = (
    ("allinone","allinone"),
    ("single-master","single-master"),
    ("multi-master","multi-master")
)

# 集群 网络 插件
K8S_CLUSTER_NETWORK = (
    ("flannel","flannel"),
    ("calico","calico"),
    ("kube-router","kube-router"),
    ("cilium","cilium")
)

# 集群节点角色
K8S_NODE_ROLE = (
    ("master","master"),
    ("backup","backup")
)

# 集群部署类型：初始部署/新增k8s节点
K8S_DEPLOY_TYPE = (
    (1,"初始"),
    (2,"新增")
)

# 集群部署状态
K8S_NODE_STATUS = (
    (1,"未部署"),
    (2,"已部署")
)

# 集群节点类型
K8S_NODE_TYPE = (
    ("k8s","k8s节点"),
    ("loadbalance","负载均衡节点"),
    ("etcd","etcd节点"),
    ("harbor","harbor节点")
)

# 集群标识
K8S_FLAG = (
    ("test","test"),
    ("uat","uat"),
    ("pro","pro")
)

# 集群初始步骤step_id
K8S_INSTALL_INIT_STEP = -100

# 集群安装 准备 操作
K8S_INSTALL_PRE = (
     (-4,"ansible环境准备"),
     (-3,"免密钥登陆配置"),
     (-2,"自定义操作"),
     (-1,"导入k8s二进制/镜像文件"),
)

K8S_INSTALL = (0,"一键安装")
K8S_INSTALL_CLEAN = (99,"清理集群")

# 集群新增节点
K8S_INSTALL_ADD_NODE = (20,"新增k8s-node节点")
K8S_INSTALL_ADD_MASTER = (21,"新增k8s-master节点")


# 集群分步安装
K8S_INSTALL_STEP = (
     (1,"安装准备"),
     (2,"安装k8s-etcd"),
     (3,"安装k8s-docker"),
     (4,"安装k8s-master"),
     (5,"安装k8s-node"),
     (6,"安装k8s-network"),
     (7,"安装k8s-plugins"),
)


# step_id 和 名称 映射
STEP_MAP = {
    -3: "install k8s-ansible",
    -2: "install k8s-ssh",
    -1: "install k8s-import",
    0: "instll k8s-onekey",
    99: "install k8s-clear",
    1: "instll k8s-prepare",
    2: "install k8s-etcd",
    3: "install k8s-docker",
    4: "install k8s-master",
    5: "install k8s-node",
    6: "install k8s-network",
    7: "install k8s-plugins",
}


# 集群部署操作每一步验证
K8S_INSTALL_CHECK = (
    (1,"kubectl version"),
    (2,"kubectl get componentstatus"),
    (3,"kubectl cluster-info"),
    (4,"kubectl get node"),
    (5,"kubectl get pod --all-namespace"),
    (6,"kubectl get svc --all-namespaces"),


)





