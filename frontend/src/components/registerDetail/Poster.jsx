/* eslint-disable prettier/prettier */
import React, { useState } from "react";
import styled, { css } from "styled-components";
import { theme } from "styled-tools";
const VALUE = {
  action: 1,
  horror: 0,
  comedy: 1,
  romance: 0,
};
const VALUE1 = {
  action: 1,
  horror: 0,
  comedy: 1,
  romance: 0,
};
export default function Poster(props) {

  

  var key = Object.keys(VALUE).filter(function(key) {return VALUE[key] === 1});
  console.log(key);
  //1을 가지고 있는 장르들의 이름(romance)를 가져온다 선택된 6가지를가져와
  //하나의 변수에 합치고 아래 result함수를 이용해서 빈도수가 많은 순서대로 나타낸다
  var key1 = Object.keys(VALUE1).filter(function(key1) {return VALUE[key1] === 1});
  console.log(key1 + "," + key);//1을 가지고 있는 장르들
  var k =key1 + "," + key;
  console.log(k);

  //빈도수를 보여준다 {"a":2,"b":2,"c":1}
  const arr = ['a', 'b', 'a', 'b', 'c'];
  const result = arr.reduce((accu, curr) => { 
    accu[curr] = (accu[curr] || 0)+1; 
    return accu;
  }, {});
  console.log(result);
  //

  const [isClicked, setIsClicked] = useState(false);
  const { prefer_ott_content_genre } = props.inputs;
  const onChangeHandler = (e) => {
    const { value, name } = e.target;
    props.setInputs({
      ...props.inputs,
      [name]: value,
    });
  };
  const handleClick = () => {
    setIsClicked(!isClicked);
  };
 
  console.log(props.inputs);
  return (
    <Wrapper isClicked={isClicked} onClick={handleClick}>
      <Title>PosterList</Title>
      <StPoster 
      src={props.imgSrc} 
      alt="poster01" 
      value={VALUE}
      name={prefer_ott_content_genre}
      onClick={onChangeHandler}
      />
    </Wrapper>
  );
}

const Wrapper = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 20rem;
  height: 33.5rem;
  ${theme("fonts.textP")}
  ${theme("neons.textNeonGold")}
  ${(props) =>
    props.isClicked
      ? css`
          color: ${theme("colors.mainPoint")};
          & > img {
            border-color: ${theme("colors.mainPoint")};
            ${theme("neons.boxNeonGold")}
          }
        `
      : css`
          &:hover {
            color: ${theme("colors.mainPoint")};

            & > img {
              border-color: ${theme("colors.mainPoint")};
              ${theme("neons.boxNeonGold")}
            }
          }
        `}
`;

const Title = styled.span`
  margin-bottom: 1.5rem;
  width: 100%;
  text-align: center;
`;

const StPoster = styled.img`
  border: 0.1rem solid ${theme("colors.mainBlack")};
  width: 20rem;
  height: 30rem;
`;
