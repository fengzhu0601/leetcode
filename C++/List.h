#include <iostream>

using namespace std;

class List{
	struct Node{
		int data;
		Node* next;
		Node(int x) : data(x), next(NULL){}
	};
	Node* head;
	int len;
public:
	List():head(NULL),len(0){
		cout << this << "********" << head << endl;
	}

	void push_front(const int& d){
		insert(d,0);
	}
	List& push_back(const int& d){
		insert(d, size());
		return *this;
	}
	int size() const{
		return len;
	}
	Node*& getptr(int pos){
		if(pos<0||pos>size()) pos = 0;
		if(pos==0) return head;
		Node* p = head;
		for(int i=1;i<pos;i++)
		{
			p=p->next;
		}
		return p->next;
//		return (*p).next;
	}
	void insert(const int& d, int pos){
		Node*& pn = getptr(pos);
		Node* p = new Node(d);
		p->next = pn;
		pn = p;
		++len;
	}

	void travel()const{
		Node* p = head;
		while(p != NULL){
			cout << p->data << ' ';
			p = p->next;
		}
		cout << endl;
	}

	void clear(){
		while(head!=NULL){
			Node* p = head->next;
			delete head;
			head = p;
		}
		len = 0;
	}

	~List(){
		cout << this << "**********" << head << endl;
		clear();
	}

	void erase(int pos){
		if(pos<0||pos>=size()) return;
		Node*& pn = getptr(pos);
		Node* p = pn;
		pn = pn->next;
		delete p;
		--len;
	}
};




