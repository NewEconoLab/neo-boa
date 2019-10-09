class DebugMap():
    addr_line = {}

    startLineMap = {}

    def addAddrLine(self,key,value):
        if key not in self.addr_line.keys() :
            self.addr_line[key] = []
            self.addr_line[key].append(value)
        else :
            self.addr_line[key].append(value)

    def addStartLine(self,methodName,startLine):
        self.startLineMap[methodName] = startLine

    def toOutString(self):
        array =[]
        for k,v in self.addr_line.items():
            m = {}
            m["name"] = k
            m["addr"] = v[0].split("-")[0]
            m["map"] = v
            array.append(m)
        return array


        
