import styled from "styled-components";
import { theme } from "styled-tools";
import { Select } from "./SelectList";

export default function BasicSelect() {
  return (
    <StInputsWrapper>
      <StInputWrapper>
        <StLabel>생년월일</StLabel>
        <StInput type="text" placeholder="ex) 0000-00-00" />
      </StInputWrapper>
      <StInputWrapper>
        <StLabel>성별</StLabel>
        <Select selectWidth="17.4rem" name="gender" form="Gender" placeholder="성별">
          <option value="1">남자</option>
          <option value="0">여자</option>
        </Select>
      </StInputWrapper>
    </StInputsWrapper>
  );
}

const StInputWrapper = styled.div`
  display: flex;
  align-items: center;
`;

const StInputsWrapper = styled(StInputWrapper)`
  justify-content: space-between;
  width: 63.4rem;
`;

const StLabel = styled.label`
  margin-right: 1.8rem;
  ${theme("fonts.textH2")}
  ${theme("neons.textNeonGold")}
`;

export const StInput = styled.input`
  border: 0.1rem solid ${theme("colors.mainWhite")};
  width: 22rem;
  color: white;
  font-family: NotoSerif;
  ${theme("fonts.textP")}
  ${theme("neons.boxNeonGold")}
`;
