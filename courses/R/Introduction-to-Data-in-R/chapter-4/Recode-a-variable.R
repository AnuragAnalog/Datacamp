# Recode cls_students as cls_type
evals_fortified <- evals %>%
  mutate(
    cls_type = case_when(
      cls_students <= 18 ~ "small",
      cls_students >= 19 & cls_students <= 59 ~ "midsize",
      cls_students > 59 ~ "large"
    )
  )
