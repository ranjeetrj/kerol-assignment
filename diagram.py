from diagrams import Cluster, Diagram, Edge
from diagrams.aws.network import PublicSubnet, NATGateway
from diagrams.aws.compute import EC2
from diagrams.aws.general import InternetGateway
from diagrams.aws.network import ElbNetworkLoadBalancer, NLB
from diagrams.aws.security import Guardduty

with Diagram("Diagram", show=False):
    IGW=InternetGateway("IGW")
    with Cluster("VPC"):
        with Cluster("Public Subnet"):
            with Cluster("NLB"):
                NetLB= NLB("NLB")
            with Cluster("Public Subnet2"):
                Pus2= NATGateway("NAT")
            with Cluster("Public Subnet1"):
                Pus1= EC2("Baston Host")

        with Cluster("Private Subnet"):
            with Cluster("Private Subnet1"):
                Pvs1= EC2("Application")
            with Cluster("SG"):
                SG = Guardduty("SG")
            with Cluster("Private Subnet2"):
                Pvs2= EC2("Application")

    IGW >> Edge(color="darkgreen") \
        << NetLB >> SG
    Pus1 >> SG
    SG >> [Pvs1, Pvs2]
    Pvs1 >> Pus2
