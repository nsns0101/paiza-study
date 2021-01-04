// 단어 s의 가운데 글자를 반환하는 함수, solution을 만들기
// 단어의 길이가 짝수면 가운데 두글자를 반환하기

public class a{

    public static String solution(String s){
        String answer = "";
        // int str_length_2_1 = s.length / 2;

        //문자열의 길이가 짝수일 때
        if(s.length() % 2 == 0){
            //string.substring(자르기 시작 값, 끝 값) 
            //ex "abcde".substring(1,3)면 bc를 반환(인덱스1, 인덱스2를 반환)
            answer = s.substring( (s.length() / 2) - 1, (s.length() / 2) + 1);  
        }
        // 문자열의 길이가 홀수일 때
        else{
            answer = s.substring( (s.length() / 2), (s.length() / 2) + 1);
        }
        return answer;
    }

    public static void main(String[] args){
        // String str = "abcde";
        String str = "abcdef";
        System.out.println(solution(str));
    }
}