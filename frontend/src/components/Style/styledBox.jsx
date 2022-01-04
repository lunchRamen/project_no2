import React from "react";
import styled from "styled-components";
import { theme } from "styled-tools";
const MenuBox = styled.ul`
  width: 50rem;
  margin: 0.8rem 0rem;
  margin-bottom: 1.2rem;
  border-radius: 1rem;
  // border: 0.1rem solid #eaeaea; 박스테두리
  box-sizing: border-box;
  // line-height: ${(props) => props.lineHeight || "4rem"};
  // background-color: ${(props) => props.backColor || "fff"};
  // padding: ${(props) => props.padding || "2rem 2.4rem"};
  ${theme("fonts.textH3")}
  ${theme("neons.textNeonGold")}
`;

function StyledBox({ children, padding, lineHeight, backColor }) {
  return (
    <MenuBox backColor={backColor} padding={padding} lineHeight={lineHeight}>
      {children}
    </MenuBox>
  );
}

export default StyledBox;
