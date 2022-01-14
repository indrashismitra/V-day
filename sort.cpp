#include <bits/stdc++.h> 
using namespace std; 
class sor { 
public: 

	string nameOfParticipant; 
	int score; 

	
	sor(string nameOfParticipant, int score) 
	{ 
		this->nameOfParticipant = nameOfParticipant; 
		this->score = score; 
	} 
}; 

class ParticipantsCompare{
    
public:
	bool operator()(const sor &a,const sor &b) 
	{ 
		
		if (a.nameOfParticipant == b.nameOfParticipant) { 
		    return a.score<b.score;
		} 
		else
		return a.nameOfParticipant<b.nameOfParticipant; 
	}
};

// Driver Code 
int main() 
{ 
	sor a("Harshita", 12); 
	sor b("Neha", 34); 
	sor c("Khushi", 10); 
	sor d("Preeti", 46); 

	list<sor> st; 
	st.push_back(a); 
	st.push_back(b); 
	st.push_back(c);
	st.push_back(d);
	ParticipantsCompare cmp;
    st.sort(cmp);
    for(auto i:st)
      cout<<i.nameOfParticipant<<" "<<i.score<<endl;
	return 0; 
} 