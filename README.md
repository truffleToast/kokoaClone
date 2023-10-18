# kokoaClone



## 10.10
- <h1>추가</h1>: 
- *= "hello" 라고 하면 hello가 들어만 있다면 
- ~= "hello" 라고 하면 앞뒤에 공백이 있는 상태에서 hello 인 경우만 선택되요.
  <span><a href="mozila.mdn">mozila</a> 에 내용 있음</span>


- "~"는 형제선택자이나 , 바로 뒤에 오지 않을 때 쓸 수 있다.
- Attribute selectors 특성 선택자
- 그냥 input과 required input이 있다면, input:required{}를 통해서, required input에만 속성을 적용시킬 수 있다.
- input{} 을 통해, [input 이름]에 해당하는 input 속성을 따로 줄 수 있다.
- 여기서, input[placeholder="First name"]은 First name에만 속성을 주지만, input[placeholder~="name"]은 name이 들어가는 모든 input에 속성을 부여할 수 있다.
- "~="은 name을 포함하고 있다는 의미가 되는 것이다.
- a[href$=".org"] → "$="는 ".org"로 끝나는 모든 anchor를 선택할 수 있다.
- attribute selectors를 이용하면, class를 지정할 필요 없이 CSS만으로 각각의 속성을 부여해줄 수 있다.
- input:required{ /* required속성을 가지고 있는 input 태그에 대해서 선택자 적용하기 */
- input[placeholder~="name"]{ /* placeHolder의 값에 "name"을 포함하는 값만 선택할 수 있다. */



## 10.09
🌼
- div:first div중 첫번째를 뜻한다.
- div:last div중 마지막 div를 고를 수 있다.
- div:nth-child("N") n번째 선택자를 고를 수 있다. <strong>even, odd 등도 사용 가능하고 2n+1 , 5n+1 등도 가능하다.</strong>
- " "은 안에 포함된 자식 선택자를 뜻한다. 블록 내부에 있는 코드를 선택할 때 사용할 수 있다.
- "+"은 바로 다음 형제 선택자. direct brother selector를 고를 때 사용할 수 있다.

## 8.31
🌼
- atrribute는 항상 "" 안에 작성.
- 어떤 태그는 id라는 arrtribute를 가질 수 있다.ex) div, image, paragraph. header, link...
- src(source)라는 attribute는 모든 태그가 가질 수 있지 않다.
- semantic 태그 사용을 지향하자.ex) header, navigation, footer...
- semantic 태그로 코드를 작성 하는 것은 매우 중요. 홈페이지의 html 문서가 훨씬 더 보기 좋고, 좋은
프로그래머가 되기 위해서는 필수 사항이다.
- header, main, footer, navigation, hgroup 등 <>속 태그들은 전부 container이다. 전부 div 태그로 쓸 수 있으나 senmantic태그를 사용하는것을 지향
- div 태그는 가장 통용적인 container이다. 대체가 가능하지만, 코드만 보고 어떤 의미인지 파악하기 위해서 semantic 태그를 쓰는 것이다.
- 모든 태그를 암기 할 필요는 없다. 필요할 때마다 문서를 찾아 적용하면 된다.
- 모르면 구글링하자

