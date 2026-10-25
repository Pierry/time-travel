import React from "react";
import {AbsoluteFill, Sequence, interpolate, spring, useCurrentFrame, useVideoConfig} from "remotion";
import {ALARMS, CAUSES, GATES, PLAN, PROMPT, STATS, VERDICT} from "./run";

// Cloud Dancer, Pantone 11-4201 TCX, approximated in sRGB.
const BG = "#F0EEE9";
const INK = "#23211C";
const MUTED = "#8A8578";
const ACCENT = "#E4572E";
const SCRIPT = "'Snell Roundhand', 'Apple Chancery', cursive";
const SANS = "'Avenir Next', 'Helvetica Neue', Arial, sans-serif";
const MONO = "Menlo, 'SF Mono', monospace";

const fade = (frame: number, start: number, len = 12) =>
  interpolate(frame, [start, start + len], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});

const rise = (frame: number, start: number) => ({
  opacity: fade(frame, start),
  transform: `translateY(${interpolate(fade(frame, start), [0, 1], [18, 0])}px)`,
});

const Kicker: React.FC<{children: React.ReactNode}> = ({children}) => (
  <div style={{fontFamily: SANS, fontSize: 22, letterSpacing: 6, color: MUTED, fontWeight: 600}}>{children}</div>
);

const Title: React.FC = () => {
  const frame = useCurrentFrame();
  return (
    <AbsoluteFill style={{justifyContent: "center", padding: 120}}>
      <div style={rise(frame, 0)}><Kicker>A PREMORTEM AGENT FOR CLAUDE CODE AND CODEX</Kicker></div>
      <div style={{...rise(frame, 6), fontFamily: SCRIPT, fontSize: 200, color: INK, lineHeight: 1.1}}>time-travel</div>
      <div style={{...rise(frame, 16), fontFamily: SANS, fontSize: 44, color: INK, fontWeight: 500}}>
        Your plan died six months from now.
      </div>
      <div style={{...rise(frame, 24), fontFamily: SANS, fontSize: 44, color: MUTED, fontWeight: 500}}>
        Here is the autopsy.
      </div>
    </AbsoluteFill>
  );
};

const Terminal: React.FC = () => {
  const frame = useCurrentFrame();
  const typed = PROMPT.slice(0, Math.max(0, Math.floor((frame - 8) / 1.2)));
  return (
    <AbsoluteFill style={{padding: 110, gap: 28, justifyContent: "center"}}>
      <div style={rise(frame, 0)}><Kicker>1. YOU TYPE ONE LINE</Kicker></div>
      <div style={{...rise(frame, 2), background: INK, borderRadius: 18, padding: "34px 40px", fontFamily: MONO, fontSize: 40, color: BG}}>
        <span style={{color: ACCENT}}>&gt; </span>{typed}
        <span style={{opacity: frame % 20 < 10 ? 1 : 0}}>▍</span>
      </div>
      <div style={{...rise(frame, 46), fontFamily: SANS, fontSize: 24, color: MUTED, fontWeight: 600, letterSpacing: 3}}>PLAN.MD, THE WHOLE INPUT</div>
      <div style={{display: "flex", flexDirection: "column", gap: 12}}>
        {PLAN.map((line, i) => (
          <div key={line} style={{...rise(frame, 52 + i * 8), fontFamily: SANS, fontSize: 34, color: INK}}>{line}</div>
        ))}
      </div>
    </AbsoluteFill>
  );
};

const Gates: React.FC = () => {
  const frame = useCurrentFrame();
  return (
    <AbsoluteFill style={{padding: 110, gap: 20, justifyContent: "center"}}>
      <div style={rise(frame, 0)}><Kicker>2. SIX LEGS, A DETERMINISTIC GATE AFTER EACH</Kicker></div>
      {GATES.map((g, i) => {
        const start = 10 + i * 14;
        return (
          <div key={g.leg} style={{...rise(frame, start), display: "flex", alignItems: "center", gap: 28, fontFamily: MONO, fontSize: 32}}>
            <div style={{width: 240, color: INK, fontWeight: 700}}>{g.leg}</div>
            <div style={{flex: 1, color: MUTED, fontFamily: SANS}}>{g.detail}</div>
            <div style={{opacity: fade(frame, start + 8, 6), color: BG, background: INK, borderRadius: 30, padding: "8px 22px", fontSize: 26}}>
              trip_lint: ok
            </div>
          </div>
        );
      })}
    </AbsoluteFill>
  );
};

const Autopsy: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  return (
    <AbsoluteFill style={{padding: 110, gap: 18, justifyContent: "center"}}>
      <div style={rise(frame, 0)}><Kicker>3. SEVEN CAUSES OF DEATH, MOST PROBABLE FIRST</Kicker></div>
      {CAUSES.map((c, i) => {
        const grow = spring({frame: frame - 10 - i * 6, fps, config: {damping: 200}});
        return (
          <div key={c.n} style={{...rise(frame, 8 + i * 6), display: "flex", alignItems: "center", gap: 22}}>
            <div style={{width: 60, fontFamily: MONO, fontSize: 26, color: MUTED}}>#{c.n}</div>
            <div style={{width: 820, fontFamily: SANS, fontSize: 28, color: INK}}>{c.name}</div>
            <div style={{flex: 1, height: 22, background: "#E2DFD7", borderRadius: 11}}>
              <div style={{width: `${c.p * grow}%`, height: 22, borderRadius: 11, background: i === 0 ? ACCENT : INK}} />
            </div>
            <div style={{width: 90, textAlign: "right", fontFamily: MONO, fontSize: 28, color: INK}}>{Math.round(c.p * grow)}%</div>
          </div>
        );
      })}
    </AbsoluteFill>
  );
};

const Verdict: React.FC = () => {
  const frame = useCurrentFrame();
  const Row: React.FC<{k: string; v: string; at: number; hot?: boolean}> = ({k, v, at, hot}) => (
    <div style={{...rise(frame, at), display: "flex", gap: 30, alignItems: "baseline"}}>
      <div style={{width: 330, fontFamily: SANS, fontSize: 26, color: MUTED, fontWeight: 600, letterSpacing: 2}}>{k}</div>
      <div style={{flex: 1, fontFamily: SANS, fontSize: 38, color: hot ? ACCENT : INK, fontWeight: hot ? 700 : 500}}>{v}</div>
    </div>
  );
  return (
    <AbsoluteFill style={{padding: 110, gap: 44, justifyContent: "center"}}>
      <div style={rise(frame, 0)}><Kicker>4. THE VERDICT, WITH EVERY LETTER</Kicker></div>
      <Row k="MOST LIKELY" v={VERDICT.likely} at={8} />
      <Row k="MOST DANGEROUS" v={VERDICT.dangerous} at={20} />
      <Row k="FATAL FLAW" v={`yes: ${VERDICT.flaw}`} at={34} hot />
    </AbsoluteFill>
  );
};

const Alarms: React.FC = () => {
  const frame = useCurrentFrame();
  const left = 180;
  const width = 1400;
  const x = (week: number) => left + (week / 26) * width;
  return (
    <AbsoluteFill style={{padding: 110}}>
      <div style={rise(frame, 0)}><Kicker>5. ONE MEASURABLE ALARM PER CAUSE, ON A WEEK</Kicker></div>
      <svg width={1800} height={760} style={{position: "absolute", left: 0, top: 200}}>
        <line x1={left} y1={420} x2={left + width * fade(frame, 4, 24)} y2={420} stroke={INK} strokeWidth={4} strokeLinecap="round" />
        <circle cx={left} cy={420} r={14} fill={BG} stroke={INK} strokeWidth={4} />
        <circle cx={left} cy={420} r={5} fill={ACCENT} />
        <text x={left} y={474} textAnchor="middle" fontFamily={SANS} fontSize={24} fill={MUTED}>today</text>
        <g opacity={fade(frame, 26)}>
          <path d={`M${left + width - 40} 420 V352 a40 40 0 0 1 80 0 V420 Z`} fill={INK} />
          <text x={left + width} y={474} textAnchor="middle" fontFamily={SANS} fontSize={24} fill={MUTED}>week 26, the day it died</text>
        </g>
        {ALARMS.map((a, i) => {
          const at = 24 + i * 10;
          const up = i % 2 === 0;
          const y = up ? 300 - (i % 3) * 40 : 540 + (i % 3) * 30;
          return (
            <g key={a.week + a.text} opacity={fade(frame, at)}>
              <line x1={x(a.week)} y1={420} x2={x(a.week)} y2={y + (up ? 26 : -40)} stroke={ACCENT} strokeWidth={2} strokeDasharray="3 8" />
              <circle cx={x(a.week)} cy={420} r={11} fill={ACCENT} />
              <text x={x(a.week)} y={up ? y - 10 : y} textAnchor="middle" fontFamily={MONO} fontSize={24} fill={ACCENT} fontWeight={700}>
                week {a.week} · cause {a.cause}
              </text>
              <text x={x(a.week)} y={up ? y + 22 : y + 32} textAnchor="middle" fontFamily={SANS} fontSize={24} fill={INK}>{a.text}</text>
            </g>
          );
        })}
      </svg>
    </AbsoluteFill>
  );
};

const Outro: React.FC = () => {
  const frame = useCurrentFrame();
  return (
    <AbsoluteFill style={{justifyContent: "center", padding: 120, gap: 50}}>
      <div style={rise(frame, 0)}><Kicker>MEASURED ON THE RECORDED RUN</Kicker></div>
      <div style={{display: "flex", gap: 110}}>
        {STATS.map((s, i) => (
          <div key={s.label} style={rise(frame, 6 + i * 8)}>
            <div style={{fontFamily: SCRIPT, fontSize: 130, color: i === 1 ? ACCENT : INK, lineHeight: 1}}>{s.value}</div>
            <div style={{fontFamily: SANS, fontSize: 28, color: MUTED, fontWeight: 600}}>{s.label}</div>
          </div>
        ))}
      </div>
      <div style={{...rise(frame, 34), background: INK, color: BG, borderRadius: 16, padding: "24px 34px", fontFamily: MONO, fontSize: 32, alignSelf: "flex-start"}}>
        claude plugin install time-travel@time-travel
      </div>
    </AbsoluteFill>
  );
};

export const SCENES = [
  {C: Title, frames: 90},
  {C: Terminal, frames: 150},
  {C: Gates, frames: 130},
  {C: Autopsy, frames: 140},
  {C: Verdict, frames: 140},
  {C: Alarms, frames: 150},
  {C: Outro, frames: 120},
];

export const TOTAL = SCENES.reduce((n, s) => n + s.frames, 0);

export const Demo: React.FC = () => {
  let from = 0;
  return (
    <AbsoluteFill style={{background: BG}}>
      {SCENES.map(({C, frames}, i) => {
        const seq = (
          <Sequence key={i} from={from} durationInFrames={frames}>
            <C />
          </Sequence>
        );
        from += frames;
        return seq;
      })}
    </AbsoluteFill>
  );
};
