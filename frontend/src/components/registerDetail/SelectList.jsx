/* eslint-disable no-unused-vars */
import React from "react";
import styled from "styled-components";
import { theme } from "styled-tools";
import { BasicSelect, DetailSelect } from "..";

export default function SelectList(props) {
  console.log(props.inputs);
  return (
    <StWrapper>
      <BasicSelect inputs={props.inputs} setInputs={props.setInputs} />
      <DetailSelect data={props.data} inputs={props.inputs} setInputs={props.setInputs} />
    </StWrapper>
  );
}
const StWrapper = styled.section`
  display: flex;
  flex-direction: column;
`;

export const Select = styled.select`
  border: 0.1rem solid ${theme("colors.mainWhite")};
  background-color: black;
  width: ${({ selectWidth }) => selectWidth};
  height: 4rem;
  color: white;
  font-family: NotoSerif;
  ${theme("fonts.textP")}
  ${theme("neons.boxNeonGold")}
`;
