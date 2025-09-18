#include <string>
#include <vector>
#include <iostream>


using namespace std;

int solution(vector<vector<string>> board, int h, int w) {

    int answer=0;
    
    cout << "board의 길이: " << board.size() << endl;
    
    vector<string> solv;
    

    
    
    if(h-1>=0) solv.push_back(board[h-1][w]);
    if(w-1>=0) solv.push_back(board[h][w-1]);
    if(w+1<board.size()) solv.push_back(board[h][w+1]);
    if(h+1<board.size()) solv.push_back(board[h+1][w]);
    
    if(!solv.empty()){
        for(int i=0; i<solv.size(); i++){
            if(solv[i]==board[h][w])
                answer++;
        }
    }
    
    
    
    return answer;

    
}