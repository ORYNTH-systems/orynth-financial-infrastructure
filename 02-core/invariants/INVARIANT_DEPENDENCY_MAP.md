# Financial Invariant Dependency Map

## Foundation

FIN-AUTH
    -> constrains FIN-ADM

FIN-ADM
    -> constrains FIN-EXE

FIN-EXE
    -> constrains FIN-EFF

FIN-EFF
    -> constrains FIN-SET

---

## Post-Effect Resolution

FIN-EFF
    -> FIN-CMP
    -> FIN-REC

FIN-EFF
    -> FIN-REV
    -> FIN-REC

FIN-SET
    -> FIN-REC
    -> FIN-FIN
    -> FIN-CON

---

## Evidence Plane

FIN-EVD spans:

FIN-AUTH
FIN-ADM
FIN-EXE
FIN-EFF
FIN-SET
FIN-CMP
FIN-REV
FIN-REC
FIN-FIN
FIN-CON
FIN-DST
FIN-JUR
FIN-AGT

Evidence supports determination.

Evidence does not create authority.

---

## Distributed Plane

FIN-DST depends upon:

FIN-AUTH
FIN-ADM
FIN-EXE
FIN-EVD

and constrains:

F2
F4
F5
F6
F7
F8

---

## Jurisdiction Plane

FIN-JUR can constrain:

FIN-AUTH
FIN-ADM
FIN-EXE
FIN-SET
FIN-DST
FIN-AGT

Jurisdictional state is not a decorative annotation.

Where jurisdiction changes admissibility, it is execution-relevant state.

---

## Autonomous Agency Plane

FIN-AGT depends upon:

FIN-AUTH
FIN-ADM
FIN-EXE
FIN-EVD
FIN-JUR

and may interact with every financial execution family.

---

## No Circular Authority Creation

No dependency edge in this architecture SHALL permit:

effect -> authority creation

settlement -> authority creation

evidence -> authority creation

consensus -> authority creation

agent capability -> authority creation

recovery requirement -> authority creation
