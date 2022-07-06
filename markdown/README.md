# 마크다운 작성법



## 1.마크다운

[**Markdown**](http://whatismarkdown.com/)은 텍스트 기반의 마크업언어로 2004년 존그루버에 의해 만들어졌으며 쉽게 쓰고 읽을 수 있으며 HTML로 변환이 가능하다. 특수기호와 문자를 이용한 매우 간단한 구조의 문법을 사용하여 웹에서도 보다 빠르게 컨텐츠를 작성하고 보다 직관적으로 인식할 수 있다. 마크다운이 최근 각광받기 시작한 이유는 깃헙([https://github.com](https://github.com/)) 덕분이다. 깃헙의 저장소Repository에 관한 정보를 기록하는 README.md는 깃헙을 사용하는 사람이라면 누구나 가장 먼저 접하게 되는 마크다운 문서였다. 마크다운을 통해서 설치방법, 소스코드 설명, 이슈 등을 간단하게 기록하고 가독성을 높일 수 있다는 강점이 부각되면서 점점 여러 곳으로 퍼져가게 된다.



## 2. 마크다운 문법

### 2.1 헤더

- 글머리: 1~6까지만 지원

```
# This is a H1
## This is a H2
### This is a H3
#### This is a H4
##### This is a H5
###### This is a H6
```



### 2.2 BlockQuote

이메일에서 사용하는 `>` 블럭인용문자를 이용한다.

```
> This is a first blockqute.
>	> This is a second blockqute.
>	>	> This is a third blockqute.
```

> This is a first blockqute.
>
> > This is a second blockqute.
> >
> > > This is a third blockqute.
> >
> > 



## 2.3 목차

#### 2.3.1**현재까지는 어떤 번호를 입력해도 순서는 내림차순으로 정의된다.**

```
1. 첫번째
3. 세번째
2. 두번째
```

#### 2.3.2 **순서없는 목차 **

```
* 1단계
  - 2단계
    + 3단계
      + 4단계
```

- 1단계
  - 2단계
    - 3단계
      - 4단계



### 2.4 코드블럭

```python
public class BootSpringBootApplication {
  public static void main(String[] args) {
    System.out.println("Hello, Honeymon");
  }
}
```



### 2.5 링크

- 참조링크

```
[link keyword][id]

[id]: URL "Optional Title here"

// code
Link: [Google][googlelink]

[googlelink]: https://google.com "Go google"
```

Link: [Google](https://google.com/)



- 외부링크

```
사용문법: [Title](link)
적용예: [Google](https://google.com, "google link")
```

Link: [Google](https://google.com%2C/)



- 자동연결

```
일반적인 URL 혹은 이메일주소인 경우 적절한 형식으로 링크를 형성한다.

* 외부링크: <http://example.com/>
* 이메일링크: <address@example.com>
```

- 외부링크: http://example.com/
- 이메일링크: [address@example.com](mailto:address@example.com)



### 2.6 이미지

```
![Alt text](/path/to/img.jpg)
![Alt text](/path/to/img.jpg "Optional title")
```

![pahkey_KRRKrp](README.assets/pahkey_KRRKrp.png)