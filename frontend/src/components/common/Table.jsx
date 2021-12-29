import styled from "styled-components";
import { theme } from "styled-tools";

//

export default function Table({ tHeadList, tBodyList }) {
  return (
    <StWrapper>
      <thead>
        <tr>
          {tHeadList.map((head, idx) => (
            <th key={`head-${idx}`}>{head}</th>
          ))}
        </tr>
      </thead>
      {tBodyList.map((body) => (
        <tbody key={`tbody-${body.id}`}>
          <tr>
            {body.contents.map((b, i) => (
              <td key={`td-${i}`}>{b}</td>
            ))}
          </tr>
        </tbody>
      ))}
    </StWrapper>
  );
}

const StWrapper = styled.table`
  border: 0.1rem solid ${theme("colors.textNeonStructure")};
  width: 144rem;
  ${theme("fonts.textP")}

  & > thead {
    color: ${theme("colors.mainPoint")};
    ${theme("neons.textNeonGold")}
  }

  & > tbody,
  td {
    cursor: pointer;
    padding: 1.5rem;
    text-align: center;
    ${theme("neons.textNeonGold")}
  }

  & > tbody {
    border: 0.1rem solid ${theme("colors.mainWhite")};
    border-radius: 1.5rem;

    &:hover {
      border-color: ${theme("colors.mainPoint")};
      ${theme("neons.boxNeonGold")};
    }
  }
`;
