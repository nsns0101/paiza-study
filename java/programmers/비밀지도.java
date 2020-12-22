//  지도는 한 변의 길이가 n 인 정사각형 배열 형태로, 각 칸은 " " 또는 "#"으로 구성되어 있다.
//  전체 지도는 두 장의 지도를 겹처서 얻을 수 있다.
//  지도1, 지도2 중 어느 하나라도 벽(#)인 부분은 전체 지도에서도 벽(#)이다.
//  지도1, 지도2에서 모두 공백인 부분은 전체 지도에서도 공백이다.
//  지도1,지도2는  # -> 0, 공백 - > 0으로 암호화 된다.
//  지도1,지도2에는 최초에 10진수로 표현되어 있다.
class Solution {
  
  public String[] solution(int n, int[] arr1, int[] arr2) {
      
      String [] answer = new String[n];
      
      for(int i=0; i<n; i++) {          
            String temp = Integer.toBinaryString(arr1[i] | arr2[i]);  
            temp = String.format("%" + n + "s", temp);
            temp = temp.replaceAll("1", "#");
            temp = temp.replaceAll("0", " ");
            answer[i] = temp;
        }
      
      return answer;
      
  }
  
}

// 십진수를 이진수로 변환하기
//     int dec = 25;
//     String binary = Integer.toBinaryString(dec);

// 비트연산
//     (4 & 5) // 4 (100,101) 을 비교하면 100(4)
//     (4 | 5) // 5 (100,101) 을 비교하면 101(5)

// ※ String format
// - String의 자릿수를 맞추는 경우, String.format("%자릿수s", str)를 이용
// - 숫자의 자릿수를 맞추는 경우, String.format("%자릿수d",num)을 이용하면 된다.