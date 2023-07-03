```mermaid
classDiagram
classA <|-- classB
classC *-- classD
classE o-- classF
classG <-- classH
classI -- classJ
classK <.. classL
classM <|.. classN
classO .. classP
```

```mermaid
flowchart TD

    A([Начало]) 
    B[Первое действие]
    C{Условие верно}
    D[Второе действие]
    E[Третье действие]

    A --> B
    B --> C
    C -->|верно| D
    C --> |не верно| E
    D --> F([Конец])
    E --> F
```

```mermaid
flowchart TB
  node1[Форма 1]  
  node2(Форма 2)
  node3([Форма 3])
  node4[[Форма 4]]
  node5[(Форма 5)]
  node6((Форма 6))
  node7>Форма 7]
  node8{Форма 8}
  node9{{Форма 9}}
  node10[/Форма 10/]
  node11[\Форма 11\]
  node12[/Форма 12\]
  node13[\Форма 13/]
```
[Mermaid live editor(Realy good)](https://mermaid.live/edit#pako:eNp9kbFOwzAQhl_FctdUKm1ZPCDRpmxMMJEwWIlDoyZx5bgqVVOJdoCFiREJIcELVIhIIESe4fxGXJpEdEB48d1_3_l--ZbUk76gjAaRnHtjrjQ5t93ETQieYweeYGvuYAtfUFxW4sCBZ8jNDbxBATmBd8jh06zNBoUPyGtquIRXsy7bKpngVTZ9Q7GqCNuBB2wqUPznnZEDL0jkZmPu_6Zqq6TdPiKD2uIuGdZOyiT7HZ8Re69AMtT23WVkVPvblU8ceER_yJjbxlJVaCaTVC8igQaCMIpYKwi6_U7HSrWSE8FavV6vjtvz0Ndj1p9eW56MpCrRoKn5PMW_V3zByEGXHFKLxkLFPPRxM8tyjkv1WMTCpQxDn6uJS91khRyfaXm2SDzKtJoJi86mPtfCDvmV4jFlAY9SVIUfaqlOq1XvNm7RKU8upGyY1Q9z6d6A)
[Mermaid habr documentation](https://habr.com/ru/articles/652867/)
[StarUML](https://staruml.io/download)
[Draw.io](https://app.diagrams.net/)
[From algorithm to code](http://www.athtek.com/flowchart-to-code.html)
