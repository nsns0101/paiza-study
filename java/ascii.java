class Solution {
    public String solution(String sentence) {
        String word = "";
        // array_word = sentence.split("");
        for(int i = 97; i <= 122; i++){
            // 소문자형태로 ascii 숫자가 들어감
            String lower = sentence.toLowerCase();

            //캐릭터형을 문자형태로( i(정수)를 캐릭터형으로)
            String abcd = Character.toString( (char)i );

            // 문자열에 abcd가 포함되는지
            if(lower.contains(abcd) ){
                continue;
            }
            else{
                word += abcd;
            }
        }
        
        if(word.length() == 0){
            return "perfect";
        }
        else {
            return word;
        }
    }
}
