// import java.util.Arrays;

public class Sort{
    public static void main(String[] args)  {
        int[] array = {1, 5, 2, 6, 3, 7, 4};
        int[][] commands = {{2, 5, 3}, {4, 4, 1}, {1, 7, 3}};
        int[] answer = new int[3];
        int answer_count = 0;
        for(int i = 0; i < commands.length; i++){
            int[] th_array = new int[3];
            int temp = 0;
            int th_arr_count = 0;
            //배열담기
            for(int j = commands[i][0]; j <= commands[i][1]; j++){
                th_array[th_arr_count] = array[j];
                th_arr_count++;
            }
            //th_array오름차순
            for(int k = 0; k < th_array.length; k++){
                for(int z=0; z < th_array.length-1; z++){
                    if(th_array[z] > th_array[z+1])
                    temp = th_array[z];
                    th_array[z] = th_array[z+1];
                    th_array[z+1] = temp;               
                }
            }
            answer[answer_count] = th_array[commands[i][2]];
            answer_count++;
            
        }
        System.out.println(answer);
    }
}



// class Solution {
//     public int[] solution(int[] array, int[][] commands) {
//         int[] answer = {};
//         int answer_count = 0;
//         for(int i = 0; i < commands.length; i++){
//             int[] th_array = {};
//             int temp = 0;
//             int th_arr_count = 0;
//             //배열담기
//             for(int j = commands[i][0]; j <= commands[i][1]; j++){
//                 th_array[th_arr_count] = array[j];
//                 th_arr_count++;
//             }
//             //th_array오름차순
//             for(int k = 0; k < th_array.length; k++){
//                 for(int z=0; z < th_array.length-1; z++){
//                     if(th_array[z] > th_array[z+1])
//                     temp = th_array[z];
//                     th_array[z] = th_array[z+1];
//                     th_array[z+1] = temp;               
//                 }
//             }
//             answer[answer_count] = th_array[commands[i][2]];
//             answer_count++;
//         }
//         return answer;
//     }
// }