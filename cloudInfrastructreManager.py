def split(data , delimeter):
    data_l = []
    s = ""
    for i in data:
        if i == delimeter:
            data_l.append(s)
            s = ""
        else:
            s += i
    data_l.append(s)
    return data_l

class Server:
    total_servers = 0
    maintenance_mode = False

    def __init__(self , hostname , ip_address , ram , cpu_cores):
        self.hostname = hostname
        self.ip_address = ip_address
        self.ram = ram
        self.cpu_cores = cpu_cores
        type(self).total_servers += 1
    def deploy(self , service_name):
        if Server.maintenance_mode == True:
            print("can't deploy during maintenance.")
        else:
            print("Deploying {} on server-{}".format(service_name , self.hostname))
    def server_info(self):
        return ("Hostname: {}\nip_address: {}\nram: {}\ncpu_cores: {}".format(self.hostname , self.ip_address , self.ram , self.cpu_cores))
    
    @classmethod
    def enable_maintenance(cls):
        cls.maintenance_mode = True
    
    @classmethod
    def disable_maintenance(cls):
        cls.maintenance_mode = False

    @classmethod
    def from_config(cls , config_string):
        server_details = split(config_string , '|')
        return cls(server_details[0] , server_details[1] , server_details[2] , server_details[3])
    
    @staticmethod
    def is_valid_ip(ip):
        ip_s = split(ip , '.')
        if len(ip_s) != 4:
            return False
        for i in ip_s:
            if int(i) < 0 or int(i) > 255:
                return False
        return True
    

class DatabaseServer(Server):

    def __init__(self , hostname , ip_address , ram , cpu_cores , database_type):
        super().__init__(hostname , ip_address , ram , cpu_cores)
        self.database_type = database_type
    def deploy(self , service_name):
        super().deploy(service_name)
        print("Starting {} service....".format(self.database_type))






s1 = Server.from_config("server-01|192.168.1.10|16|8")

db = DatabaseServer(
    "db-01",
    "192.168.1.50",
    32,
    16,
    "PostgreSQL"
)

Server.enable_maintenance()

s1.deploy("Redis")

Server.disable_maintenance()

db.deploy("Inventory API")

print(Server.total_servers)

print(Server.is_valid_ip("256.100.1.1"))

print(Server.is_valid_ip("192.168.1.5"))