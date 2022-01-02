import React from "react";
import styled from "styled-components";
import { theme } from "styled-tools";
const StyledInput = styled.input`
  /* 공통 스타일 */
  width: 100%;
  outline: none;
  border: 0.1rem solid #ededed;
  box-sizing: border-box;
  color: #333;
  padding-left: 1rem;
  padding-right: 1rem;

  /* 색상 */
  // background: black;
  color: white;
  /* 크기 */
  height: 4rem;
  margin-top: 0.5rem;
  border-radius: 1.2rem;
  ${theme("fonts.textH4")} ${theme("neons.boxNeonGold")};
`;

const LoginInput = function ({ type, name, placeholder, onChange, value }) {
  return <StyledInput type={type} name={name} placeholder={placeholder} onChange={onChange} value={value} />;
};

export default LoginInput;
