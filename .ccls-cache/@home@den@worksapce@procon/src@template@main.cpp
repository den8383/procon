#include <bits/stdc++.h>
using namespace std;

int main(){
  int num;
  cin >> num;
  vector<string> lines(num);
  for(int i = 0; i < num; i++){
    cin >> lines.at(i);
  }
  for(auto line: lines){
    cout << line << endl;
  }

  return 0;
}
