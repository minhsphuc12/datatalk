setwd("~/git/datatalk/world_cup")
require(tidyverse)
wc = read_csv('C:/Users/Nasdap/Documents/git/datatalk/world_cup/WorldCups.csv')
match = read_csv('C:/Users/Nasdap/Documents/git/datatalk/world_cup/WorldCupMatches.csv')
player = read_csv('C:/Users/Nasdap/Documents/git/datatalk/world_cup/WorldCupPlayers.csv')

# how many times each countries get into a depth level of world cup -----
table(match$Stage)
match_depth = match %>%
  mutate('depth' = 
           case_when(
             grepl('Group', Stage) ~ 1,
             Stage %in% c('Round of 16', 'Preliminary round', 'First round') ~ 2,
             Stage == 'Quarter-finals' ~ 3,
             Stage == 'Semi-finals' ~ 4,
             Stage == 'Final' ~ 5,
             T ~ NA_real_
           )
         ) %>%
  filter(!is.na(depth))

# mapping with density of how many time each country get in world cup -----
country_participate = union_all(match %>% group_by(Year, `Home Team Name`, `Home Team Initials`) %>% summarise() %>%
                                  rename(team_name = `Home Team Name`, team_initial = `Home Team Initials`),
                                match %>% group_by(Year, `Away Team Name`, `Away Team Initials`) %>% summarise() %>%
                                  rename(team_name = `Away Team Name`, team_initial = `Away Team Initials`)) %>%
  group_by(Year, team_name, team_initial) %>%
  summarise() %>%
  group_by(team_name, team_initial) %>%
  summarise(count = n()) %>%
  arrange(desc(count))

### another example of world map -------
# http://www.statsoft.org/wp-content/uploads/2016/09/Lecture6_HKMapVis.html#world-map
# install.packages('maps')
library(maps)
a = maps::unemp
library(ggplot2)
thismap = map_data(map = "world")
thismap_update = left_join(thismap, country_participate, by = c('region' = 'team_name')) %>%
  mutate(count = ifelse(is.na(count), 0, count))

## maybe some country gone missing when we are dealing with somewhat non-stardard feature like country name.
# best to have ISO or country code to merge.
thismap_update_check = thismap_update %>% group_by()

# install.packages('ggrepel')
require(ggrepel)

ggplot(thismap_update %>% filter(region != 'Antarctica'), aes(long, lat, group=group, fill = count)) + 
  geom_polygon() +
  ggrepel::geom_label_repel(data = thismap_update %>% filter(count > 10) %>%
                              group_by(region) %>%
                              filter(row_number() == 1),
                            aes(long, lat, label = paste0(region, ' :', count)), fill = 'white') +
  scale_fill_continuous(low = 'white', high = 'firebrick') +
  labs(x = NULL, y = NULL,
       title = 'Sound American is the hottest continent for World Cup',
       subtitle = 'Most of South American and European countries have appeared in World Cup',
       caption = 'source: Kaggle.com') +
  theme(axis.ticks.x = element_blank(), axis.text.x=element_blank(),
        axis.ticks.y = element_blank(), axis.text.y=element_blank())



## easy EDA univariate -----
a = sort(table(match$`Home Team Name`, useNA = 'ifany'), decreasing = T)
a = data.frame(a)
a %>% ggplot() +
  geom_col(aes(Var1, Freq, group = 1)) +
  coord_flip()
