// 전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.

// 전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.

// 구조대 : 119
// 박준영 : 97 674 223
// 지영석 : 11 9552 4421

// 전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때,
// 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.

// 입출력 예 #1
// 앞에서 설명한 예와 같습니다.

// 입출력 예 #2
// 한 번호가 다른 번호의 접두사인 경우가 없으므로, 답은 true입니다.

// 입출력 예 #3
// 첫 번째 전화번호 “12”가 두 번째 전화번호 “123”의 접두사입니다. 따라서 답은 false입니다.

import java.util.Arrays;

class Solution {
    public boolean solution(String[] phone_book) {
        // 기본값 true로 설정
        boolean answer = true;

        //배열을 정렬
        Arrays.sort(phone_book);
        
        //
        for(int i = 0; i < phone_book.length - 1; i++){
            for (int j = i + 1; j < phone_book.length; j++){
                //접두어인 경우에 false 아니면 기본값인 true를 그대로 
                if(phone_book[j].contains(phone_book[i])){
                    return answer = false;   
                }
            }
        }
        return answer;
    }
}