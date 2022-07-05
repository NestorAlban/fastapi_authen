

class Mapping_rath():
    def __init__(self) -> None:
        pass

    
    
    def role_mapping(role: int):
        print("=========role===============")
        roles = {
            0: "user",
            1: "worker level 1",
            2: "worker level 2",
            3: "worker level 3"
        }
        role_name = None
        
        print(f'{role} got')
        if role in roles:
            print("exist")
            role_name = roles.get(role)
        else:
            print("existn")
        print("=========role===============")
        return role_name

    def status_mapping(stat: int):
        print("=========status===============")
        status = {
            0: "eliminado",
            1: "registrado",
            2: "premium",
            3: "special"
        }
        status_name = None
        
        print(f'{stat} got')
        if stat in status:
            print("exist")
            status_name = status.get(stat)
        else:
            print("existn")
        print("=========status===============")
        return status_name


    


