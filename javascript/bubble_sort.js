// 정수를 포함하고 아직 길이가 결정되지 않은 배열이 있는 경우.
// 루프, if, 다른 문 등을 사용하여 정수를 정렬하는 사용자 정의 정렬 함수를 생성하십시오.
// 오름차순

var sort = function(array) {
    var temp;
    for (var i = 0; i < array.length - 1; i++) {        // 순차적으로 비교하기 위한 반복문
      for (var j = 0; j < array.length - 1 - i; j++) {  // 끝까지 돌았을 때 다시 처음부터 비교하기 위한 반복문
        if (array[j] > array[j + 1]) {                  // 두 수를 비교하여 앞 수가 뒷 수보다 크면
          temp = array[j];                              // 두 수를 서로 바꿔준다
          array[j] = array[j + 1];
          array[j + 1] = temp;
        }
      }
    }
    return array;
  };
  
sort([5,1,7,4,6,3,2,8]);
console.log(sort([5,1,7,4,6,3,2,8.9,2,4,1,3,2]));