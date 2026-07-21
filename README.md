# AIP Swarm Project — Contribution Case Study

ROS 2 Humble 기반 군집 순찰 로봇 팀 프로젝트에서 제가 담당한 **카메라 비전, 웹 관제, 서브 차량 구동**을 설명하는 공개 case study입니다.

> This repository documents my scoped contribution to a team-built ROS 2 swarm system. It does not present the complete team system as my individual work.

## Why This Repository Exists

원본 `aip-swarm-ws`는 팀 프로젝트 저장소입니다. 팀의 공개·제출 동의를 받았지만, 전체 코드를 복제해 개인 프로젝트처럼 보이게 하는 대신 본인 기여와 팀 시스템의 경계를 명확히 공개합니다.

## Project Context

- ROS 2 Humble 기반 다중 차량 순찰 시스템
- Gazebo Ignition, Nav2, FastDDS Discovery Server, Foxglove/Web dashboard
- RGB·열화상 인식과 중앙 관제
- 실차와 시뮬레이션을 단계적으로 통합하는 팀 프로젝트

```text
Vehicle sensors / cameras
        │
        ├── ROS 2 perception topics ──> central monitoring
        ├── vehicle state / alerts ───> web dashboard
        └── drive commands ───────────> scout vehicle control path
```

## My Contribution

| 구분 | 담당 내용 | 관련 원본 모듈 |
|---|---|---|
| 본인 수행 | 웹 관제 서버와 화면 | `aip_fleet_dashboard`, `FleetDashboard.tsx` |
| 본인 수행 | 카메라·인식 결과의 관제 연동 | `aip_fleet_perception`, `PerceptionAlert` 인터페이스 |
| 본인 수행 | 서브 차량 구동 연동 | scout firmware·구동 명령 경로 |
| 공동 수행 | 위 기능을 팀 ROS 2 graph와 통합·시험 | 팀 launch/config와 인터페이스 조율 |
| 팀 시스템 | Gazebo world, Nav2 전체 구성, `gz_ros2_control` 기반 제어 | 개인 성과로 주장하지 않음 |

자세한 경계는 [CONTRIBUTIONS.md](CONTRIBUTIONS.md)를 참고하십시오.

## Technical Decisions I Can Explain

### 1. 관제와 로봇 제어의 경계

웹 관제는 로봇의 상태와 경보를 표시하고 명령을 전달하지만, 실제 속도 제한과 안전 정지는 로봇 측 제어 경로가 책임지도록 분리했습니다. UI 연결 상태가 로봇 안전 상태를 대신하지 않도록 한 결정입니다.

### 2. 카메라 결과의 공통 메시지화

카메라·열화상 처리 결과를 중앙 관제가 소비할 수 있도록 detection 결과와 경보를 ROS 2 인터페이스로 분리했습니다. 관제 화면이 특정 detector 내부 구현에 직접 의존하지 않게 하는 목적입니다.

### 3. 서브 차량의 독립성

서브 차량은 자신의 namespace와 구동 인터페이스를 유지하고 중앙 시스템은 계약된 토픽을 통해 상태와 명령을 교환하도록 구성했습니다.

## Evidence Policy

- 원본 저장소의 많은 커밋이 공용 `AIP Team` 저자로 기록되어 commit count를 개인 기여 증거로 사용하지 않습니다.
- 팀 동의가 확인된 문서와 설명을 공개했으며, 원본 전체 코드는 이 저장소에 복제하지 않았습니다.
- 코드나 영상은 팀 합의 범위와 개인 기여 경계가 확인된 자료만 이후 추가합니다.

## Current Limitations

- 이 저장소는 실행 가능한 전체 swarm workspace가 아니라 contribution case study입니다.
- `gz_ros2_control` 설정과 관련 장애 해결은 팀 시스템 설명에 포함되지만 제 개인 구현으로 표시하지 않습니다.
- 정량 성능은 원본 실험 로그가 개인 담당 기능과 직접 연결되는 경우에만 추가할 예정입니다.

## Interview Summary

- **30초:** “군집 시스템 전체를 제가 만들었다고 주장하지 않고, 팀 안에서 제가 맡은 카메라 비전·웹 관제·서브 차량 구동의 인터페이스와 통합 경험을 정리했습니다.”
- **3분:** 문제 정의 → 담당 경계 → ROS 2 인터페이스 → 관제와 제어의 안전 경계 → 팀 통합 과정 순서로 설명합니다.

## Related Portfolio

- [ROS 2 Robot Systems Software Portfolio](https://github.com/spongebobDG/robotics-software-portfolio)
- [TurtleBot Fleet Ops](https://github.com/spongebobDG/turtlebot-fleet-ops)
