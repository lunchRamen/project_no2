/* eslint-disable no-unused-vars */
/* eslint-disable prettier/prettier */
import React, { useState, useEffect } from "react";
import { client } from "../../libs";
import styled from "styled-components";
import { Poster } from "..";

export default function PosterList(props) {
  const [poster, setPoster] = useState([]);

var key = Object.keys(poster).filter(function (key) {
  return poster[key] === 1;
});
console.log(key);
// //1을 가지고 있는 장르들의 이름(romance)를 가져온다 선택된 6가지를가져와
// //하나의 변수에 합치고 아래 result함수를 이용해서 빈도수가 많은 순서대로 나타낸다

// var key1 = Object.keys(VALUE1).filter(function (key1) {
//   return VALUE[key1] === 1;
// });
// console.log(key1 + "," + key); //1을 가지고 있는 장르들
// var k = key1 + "," + key;
// console.log(k);

// //빈도수를 보여준다 {"a":2,"b":2,"c":1}
// const arr = ["a", "b", "a", "b", "c"];
// const result = arr.reduce((accu, curr) => {
//   accu[curr] = (accu[curr] || 0) + 1;
//   return accu;
// }, {});
// console.log(result);

  useEffect(() => {
    fetchPoster();
  }, []);

  const fetchPoster = async () => {
    const { data } = await client.get("/user/contents-list");
    setPoster(data);
  };
  console.log(poster);
  return (
    <Wrapper>
        {poster && poster.map((poster, idx)=> (
          <Poster
          key={`poster-${idx}`}
          imgSrc={poster.img_link}
          />
        ))}
    </Wrapper>
  );
}

const Wrapper = styled.div`
  display: flex;
  flex-wrap: wrap;
  width: 95rem;
  row-gap: 5rem;
  column-gap: 4.5rem;
`;

