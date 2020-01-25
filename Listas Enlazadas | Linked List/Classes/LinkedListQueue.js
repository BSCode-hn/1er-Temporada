function Queue(){
    this.first = null;
    this.add = QueueAdd;
    this.delete = QueueDelete;
    this.print = QueuePrint;
}

    function QueueAdd(value){
        if (!this.first){
            this.first = new Node(value);
            return true;
        }else{
            current = this.first;
            while(current.next){
                current = current.next;
            }
            current.next = new Node(value);
            return true;
        return false;
        }
    }

    function QueueDelete(){
        if (!this.first){
            return false;
        }else{
            current = this.first;
            this.first = this.first.next;
            return true;
        }
    }

    function QueuePrint(){
        trail = "";
        current = this.first;
        while(current){
            trail += current.value;
            trail += "-->";
            current = current.next;
        }
        trail += "null";
        return trail;
    }