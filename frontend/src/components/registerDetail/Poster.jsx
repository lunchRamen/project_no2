import React, { useState } from "react";
import styled, { css } from "styled-components";
import { theme } from "styled-tools";
// import { client } from "../../libs";
const VALUE = {
  action: 1,
  horror: 0,
  comedy: 1,
  romance: 0,
};
// const VALUE1 = {
//   action: 1,
//   horror: 0,
//   comedy: 1,
//   romance: 0,
// };
export default function Poster(props) {
  // const [poster, setPoster] = useState([]);
  // const fetchPoster = async () => {
  //   const { data } = await client.get("/user/contents-list");
  //   console.log(data[0].img_link);
  // };
  //   for (let i = 0; i < poster.length; i++) {
  //     console.log(poster[i]);
  // }
  // useEffect(() => {
  //   fetchPoster();
  // }, []);

  const [isClicked, setIsClicked] = useState(false);
  // const { prefer_ott_content_genre } = props.inputs;
  // const onChangeHandler = (e) => {
  //   const { value, name } = e.target;
  //   props.setInputs({
  //     ...props.inputs,
  //     [name]: value,
  //   });
  // };
  const handleClick = () => {
    setIsClicked(!isClicked);
  };
  return (
    <Wrapper isClicked={isClicked} onClick={handleClick}>
      <Title>PosterList</Title>
      <StPoster
        src={props.imgSrc}
        alt="poster01"
        value={VALUE}
        // name={prefer_ott_content_genre}
        // onClick={onChangeHandler}
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
