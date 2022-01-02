import React from "react";
import styled from "styled-components";
import { theme } from "styled-tools";
const StyledLabel = styled.label`
  color: white;
  padding-left: 5px;
`;
const StyledInput = styled.input`
  /* 공통 스타일 */
  width: 95%;
  outline: none;
  border: 0.1rem solid #ededed;
  border-radius: 1.2rem;
  box-sizing: border-box;
  color: #333;
  padding-left: 0.5rem;
  padding-right: 0.5rem;

  /* 색상 */
  background: black;
  color: white;

  /* 크기 */
  height: 4rem;
  margin: 0.4rem 1rem 0rem 1rem;
  ${theme("fonts.textH4")} ${theme("neons.boxNeonGold")};
`;

const RegisterInput = function ({ labelName, name, type, placeholder, onChange, value }) {
  return (
    <StyledLabel>
      {labelName}
      <StyledInput name={name} type={type} placeholder={placeholder} onChange={onChange} value={value} />
    </StyledLabel>
  );
};

export default RegisterInput;
