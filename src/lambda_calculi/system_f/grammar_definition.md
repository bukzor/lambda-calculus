```
(kinds) κ ::= ∗|κ₁ → κ₂
(types) τ ::= α|τ₁ → τ₂|∀α:κ.τ|λα:κ.τ|τ₁ τ₂
(terms) e ::= x|λx:τ.e|e₁ e₂|Λα:κ.e|e τ
(environments) Γ ::= ⟨⟩|Γ,(x:τ)|Γ,(α:κ)
```