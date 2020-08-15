//howtoliveworldnice.tistory.com
#include<stdio.h>
#include<stdint.h>
struct Data{
	int val;
	Data(int k=-1):val(k){}
	void print(){
		printf("%d\n",val);
	}
};
class XLL{
	private:
		struct Node{
			Data d;
			Node*both;
			Node():d(Data()),both(NULL){}
		};
		Node*head,*tail;
		int cnt; //number of elements
		
	public:
		XLL():cnt(0),head(NULL),tail(NULL){}
		int getCnt(){return cnt;}
		void addElement(Data d);
		Data getElement(int idx);
};
void XLL::addElement(Data d){
	Node*n = new Node();
	n->d=d;
	if(cnt>0){
		uintptr_t tail_both=(uintptr_t)tail->both;
		n->both = tail;
		tail_both ^= (uintptr_t)n;
		tail->both = (Node*) tail_both;
		tail=n;
	}
	else head=tail=n;
	++cnt;
}
Data XLL::getElement(int idx){
	Data d;
	if(idx>=0 && idx<cnt){
		Node*cur=head,*nxt=head->both;
		//until the index becomes idx
		for(int i=0;i<idx;i++){
			uintptr_t temp=(uintptr_t)cur ^(uintptr_t)nxt->both;
			cur=nxt;
			nxt=(Node*)temp;
		}
		d=cur->d;
	}
	return d;
}
int main(){
	XLL List; Data d;
	List.addElement(Data(1));
	List.addElement(Data(5));
	List.addElement(Data(3));
	d=List.getElement(1);
	List.addElement(Data(777));
	d=List.getElement(3);
	d.print();
}
