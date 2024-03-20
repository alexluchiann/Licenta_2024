import openstack

class OpenstackConnect:
    def __init__(self):
        self.conn=openstack.connect(cloud='openstack')

    def List_All_VM(self):
        list_VM= [VM_Info for VM_Info in self.conn.compute.servers()]
        return list_VM

    def Delete_VM(self,name_VM):
        try:
            targ = self.conn.compute.find_server(name_VM)
            self.conn.compute.delete_server(targ,ignore_missing=True)
            print("Deleted {} instance ".format(name_VM))
        except Exception as e:
            print(" Instance {} doesen't exist".format(name_VM))


app=OpenstackConnect()
for i in app.List_All_VM():
    print(i.name)

app.Delete_VM('Test_2')